import cf_api
import problem_difficulty

contestID = 101

solvedf = cf_api.getProblemDataFromContest(contestID)
solvedf.to_csv('problemdata.csv', index=False)

problemdf = cf_api.getSolveSuccessDF(contestID)
problemdf.to_csv('solvedata.csv', index=False)

fullDF = problem_difficulty.save_contest_info()
fullDF.to_csv('full_frame.csv', index=False)
