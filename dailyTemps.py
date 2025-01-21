def dailyTemperatures(temperatures):
    res = [0]*len(temperatures)
    stack = []

    for i,j in enumerate(temperatures):
        while stack and j > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i-stackInd)
        stack.append([j,i])
    return res