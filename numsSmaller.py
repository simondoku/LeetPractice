def smallerNumsThanI(nums):
    dict = {}
    temp = sorted(nums)
    for i, v in enumerate(temp):
        if v not in dict:
            dict[v] = i
    res = []
    for i in nums:
        res.append(dict[i])
    return res

nums = [8, 1, 2, 2, 3]
print(smallerNumsThanI(nums))