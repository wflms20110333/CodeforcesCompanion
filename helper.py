
def gen_id(contestID, problemID):
    return int(contestID) * 26 + ord(problemID[0]) - 65