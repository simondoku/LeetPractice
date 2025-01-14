import unittest
def productSubarray(nums, k):
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