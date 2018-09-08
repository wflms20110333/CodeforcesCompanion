import requests
import pandas as pd
import cf_api

contestID = 101
url = 'http://codeforces.com/api/contest.standings?contestId=' + str(contestID) + '&from=1&count=1'
r = requests.get(url).json()['result']

problems = r['problems']
probdf = pd.DataFrame.from_dict(problems)
contest = r['contest']['name']

probdf['contestID'] = contestID
probdf['contestName'] = contest

probdf.to_csv('test.csv', index=False)

solvedf = cf_api.getProblemDataFromContest(contestID)
solvedf.to_csv('solve.csv', index=False)

problemdf = cf_api.getSolveSuccessDF(contestID)
problemdf.to_csv('problem.csv', index=False)