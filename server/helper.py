
def gen_id(contestID, problemID):
    return int(contestID) * 260 + (ord(problemID[0]) - 65) * 10 + (int(problemID[1]) if len(problemID) == 2 else 0)
