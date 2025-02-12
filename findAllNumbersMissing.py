def allMissingNums(nums):
    res = []
    set_nums = set(nums)

    for i in range(1, len(nums)+1):
        if i not in set_nums:
            res.append(i)
    return res

nums = [4,3,2,7,8,2,3,1]
print(allMissingNums(nums))
