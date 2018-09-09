#Adapted from yjiao's application of the CF API (https://github.com/yjiao/codeforces-api)
from database import query_tag, get_rating
import numpy as np
import pandas as pd
import cf_api

# Adaptation of Rating Formula from Codeforces (https://codeforces.com/blog/entry/102)
def get_solve_probability(userRating, problemRating):
    return 1.0 / (1.0 + np.power(10, (problemRating - userRating) / 400.0))

def gen_id(contestID, problemID):
    return int(contestID) * 260 + (ord(problemID[0]) - 65) * 10 + (int(problemID[1]) if len(problemID) == 2 else 0)

def save_contest_info():
    contestList = cf_api.getContestList()
    numAdded = 0
    fullFrame = pd.DataFrame(columns=['contestID', 'problemID','rating','tags'])
    for ID in contestList:
        contest_df = get_contest_elo(ID)
        if(contest_df is None):
            continue

        print('Added: ' + str(ID))
        numAdded += 1

        fullFrame = fullFrame.append(contest_df)

    return fullFrame

def get_contest_elo(contestID):
    try:
        contest_df = cf_api.getSolveSuccessDF(contestID)
    except:
        return None
    if(contest_df is None):
        return None
    if(contest_df.shape[0] < 50):
        return None

    contestID = contest_df.contestID.unique()[0]
    uniqProbs = contest_df.problemID.unique()
    tags_df = cf_api.getProblemDataFromContest(contestID)
    currProblem = 0
    data = {}
    data['contestID'] = []
    data['problemID'] = []
    data['rating'] = []
    data['tags'] = []

    for pi in uniqProbs:
        pr = get_problem_elo(contest_df[contest_df.problemID == pi])

        data['contestID'].append(contestID)
        data['problemID'].append(pi)
        data['rating'].append(pr)
        data['tags'].append(tags_df['tags'][currProblem])
        currProblem += 1

    return pd.DataFrame(data)

def process_probability(r):
    return get_solve_probability(r['rating'], r['problemRating'])

MIN_RATING = 0
MAX_RATING = 4000
MAX_ITER = 15

def get_problem_elo(problem_df):
    numSolved = np.sum(problem_df.success)

    lo = MIN_RATING
    hi = MAX_RATING

    for i in range(MAX_ITER):
        mid = (lo + hi) / 2.0
        problem_df['problemRating'] = mid
        expectedSolves = np.sum(problem_df.apply(process_probability, axis=1))

        if expectedSolves > numSolved:
            lo = mid
        else:
            hi = mid

    return int(round((lo + hi) / 2.0))

def get_user_elo(subdf, category_problems):
    if not len(category_problem):
        return 1500

    numSolved = 0
    for index, r in subdf.rows():
        look_id = gen_id(r['contestID'], r['problemID'])
        if category_problems[look_id]:
            numSolved += 1
            r['rating'] = get_rating(look_id)

    lo = MIN_RATING
    hi = MAX_RATING

    for i in range(MAX_ITER):
        projected_elo = (lo + hi) / 2.0
        expectedSolves = 0
        for index, r in subdf.rows():
            if category_problems[gen_id(r['contestID'], r['problemID'])]:
                expectedSolves += get_solve_probability(projected_elo, r['rating'])
        if expectedSolves > numSolved:
            lo = mid
        else:
            hi = mid
    return int(round((lo + hi) / 2.0))


categories = ['expression parsing','fft','two pointers','binary search','dsu','strings','number theory','data structures',
    'hashing','shortest paths','matrices','string suffix structures','graph matchings','dp','dfs and similar','meet-in-the-middle',
    'games','schedules','constructive algorithms','greedy','bitmasks','divide and conquer','flows','geometry','math',
    'sortings','ternary search','combinatorics','brute force','implementation','2-sat','trees','probabilities','graphs',
    'chinese remainder theorem']

def suggest_problem(category, handle):
    if(not cf_api.isValidUser(handle)):
        raise ValueError("Invalid Handle")
    if(category not in categories):
        raise ValueError("Invalid Error")

    subdf = cf_api.getUserSubmissions(handle)
    category_problems = query_tag(category)
    personal_rating = get_user_elo(subdf, category_problems)
    res = ''
    best_problem_rating = 0

    for index, r in subdf.rows():
        look_id = gen_id(r['contestID'], r['problemID'])
        if category_problems[look_id]:
            return r['contestID'], r['problemID']
    return subdf[0]['contestID'], subdf[0]['problemID']

PERCENT_MISS = 0.2

def get_partial(chance, wa):
    return max(0, chance * (1-wa * PERCENT_MISS))
def get_partial_credit(r):
    return np.max(0.0, r['solved'] - PERCENT_MISS * r['wrongSubs'])
