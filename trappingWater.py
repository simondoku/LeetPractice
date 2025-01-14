import unittest

def trappingRain(height: list[int]) -> int:
    '''
    Two Pointer Approach: TC: O(n), SC: O(1)
    Intialize two pointers:
        -left = 0 and right = n-1
        -left_max and right_max to keep track of the max at both sides
    Move the Pointer inwards:
        -if the height[left] < height[right]
        --if the height[left] >= left_max: update left
        --else water trapped = left_max - height[left]
        --move left rightward
        -if height[right] > right_max: update right
        --else water trapped = right_max - height[right]
        --move right leftward
    Return Water Trapped

    '''
    
    left, right = 0, len(height)-1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max-height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max-height[right]
            right -= 1
    return water_trapped


class TestingTrappingRain(unittest.TestCase):
    def testCases(self):
        self.assertEqual(trappingRain([0,2,0,3,1,0,1,3,2,1]), 9)
        self.assertEqual(trappingRain([3, 0, 2, 0, 4]), 7)
        self.assertEqual(trappingRain([]), 0)

if __name__ == "__main__":
    unittest.main()

