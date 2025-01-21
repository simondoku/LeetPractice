import unittest
def productSubarray(nums: list[int], k: int) -> int:
    '''
    Initialize Pointers and Variables:
        left = 0: Start of the sliding window.
        product = 1: Keeps track of the product of elements in the current window.
        count = 0: Counts the number of valid subarrays.

    Expand the Window (Right Pointer):
        Iterate through the array with a right pointer.
        Multiply product by nums[right].

    Shrink the Window if Product ≥ k:
        If product becomes greater than or equal to k, 
        shrink the window by moving left to the right and dividing product by nums[left].
    
    Count Subarrays:
        For every valid window, the number of valid subarrays ending at right is (right - left + 1).
    '''
    if k <= 1:
        return 0
    left = 0
    count = 0
    product = 1

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left] 
            left += 1
        
        count += (right - left + 1)
    return count
    
class TestProductSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(productSubarray([10,5,2,6], 100), 8)
        self.assertEqual(productSubarray([1, 2, 3], 0), 0)

    def test_edge_cases(self):
        self.assertEqual(productSubarray([], 100), 0)
        self.assertEqual(productSubarray([1, 2, 3], -1), 0)
        self.assertEqual(productSubarray([1, 2, 3], 1), 0)
        self.assertEqual(productSubarray([1, 2, 3], 6), 4)
        self.assertEqual(productSubarray([1, 2, 3, 4], 24), 8)

if __name__ == '__main__':
    unittest.main()

'''
Time complexity: O(n)
Space Complexity: O(1)
'''