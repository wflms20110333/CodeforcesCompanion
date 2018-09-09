import cf_api
import re

contestID = 101

solvedf = cf_api.getProblemDataFromContest(contestID)
solvedf.to_csv('problemdata.csv', index=False)

problemdf = cf_api.getSolveSuccessDF(contestID)
problemdf.to_csv('solvedata.csv', index=False)

handle = 'm1sch3f'
print(cf_api.isValidUser(handle))
subdf = cf_api.getUserSubmissions(handle)
subdf.to_csv('subdata.csv', index=False)