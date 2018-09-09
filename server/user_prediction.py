import numpy as np
import pandas as pd
import cf_api
import pandas as pd

categories = ['expression parsing','fft','two pointers','binary search','dsu','strings','number theory','data structures',
    'hashing','shortest paths','matrices','string suffix structures','graph matchings','dp','dfs and similar','meet-in-the-middle',
    'games','schedules','constructive algorithms','greedy','bitmasks','divide and conquer','flows','geometry','math',
    'sortings','ternary search','combinatorics','brute force','implementation','2-sat','trees','probabilities','graphs',
    'chinese remainder theorem']

def suggest_problem(category, handle):
    skill, finished_problems = estimate_skill(category, handle)


def estimate_skill(category, handle):
    if(not cf_api.isValidUser(handle)):
        raise ValueError("Invalid Handle")
    if(category not in categories):
        raise ValueError("Invalid Error")

    subdf = cf_api.getUserSubmissions(handle)

    category_problems = {}



PERCENT_MISS = 0.2
def get_partial_credit(r):
    return np.max(0.0, r['solved'] - PERCENT_MISS * r['wrongSubs'])