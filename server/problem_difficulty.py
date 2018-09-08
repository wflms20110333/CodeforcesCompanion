#Adapted from yjiao's application of the CF API (https://github.com/yjiao/codeforces-api)
import numpy as np
import cf_api

#Adaptation of Rating Formula from Codeforces (https://codeforces.com/blog/entry/102)
def get_solve_probability(userRating, problemRating):
    return 1.0 / (1.0 + np.power(10, (problemRating - userRating) / 400.0))

def save_contest_info():
    contestList = cf_api.getContestList()

    for ID in contestList:
        contest_df = get_contest_elo(ID)
        if(contest_df == None)
            continue



def get_contest_elo(contestID):
    contest_df = cf_api.getSolveSuccessDF(contestID)
    if(contest_df == None)
        return None






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
