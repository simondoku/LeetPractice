def canSeePersonCount(heights):
    n = len(heights)
    res = [0]* n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and heights[i] > heights[stack[-1]]:
            stack.pop()
            res[i] += 1

        if stack:
            res[i] += 1
        
        stack.append(i)
    return res

height = [10, 6, 8, 5, 11, 9]
print(canSeePersonCount(height)==[3, 1, 2, 1, 1, 0])