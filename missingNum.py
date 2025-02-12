def missingNums(nums):
    n = len(nums)
    return sum(range(n+1)) - sum(nums)
# Time complexity: O(n)