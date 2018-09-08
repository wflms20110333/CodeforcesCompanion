#Adapted from yjiao's application of the CF API (https://github.com/yjiao/codeforces-api)
import numpy as np
import pandas as pd
import cf_api

# Adaptation of Rating Formula from Codeforces (https://codeforces.com/blog/entry/102)
def get_solve_probability(userRating, problemRating):
    return 1.0 / (1.0 + np.power(10, (problemRating - userRating) / 400.0))

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
