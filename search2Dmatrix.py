def searchMatrix(matrix, target):
    def binarySearch(left, right, row, target):
        while left <= right:
            mid = left + (right-left)//2
            if  row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        return False
            
    for row in matrix:
        left, right = 0, len(row)-1
        if binarySearch(left, right, row, target):
            return True
            
    return False