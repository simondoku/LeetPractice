def search(nums, target):
    left, right = 0, len(nums)-1
    #nums is already sorted
    while left <= right:
        mid = left + ((right-left)//2)
        if nums[mid] > target:
            right = mid-1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid       
    return -1
