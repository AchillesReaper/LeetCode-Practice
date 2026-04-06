'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

'''

from termcolor import cprint
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0
        
        # left, right = 0, len(height) - 1
        # left_max, right_max = height[left], height[right]
        # trapped_water = 0
        
        # while left < right:
        #     if left_max < right_max:
        #         left += 1
        #         left_max = max(left_max, height[left])
        #         trapped_water += max(0, left_max - height[left])
        #     else:
        #         right -= 1
        #         right_max = max(right_max, height[right])
        #         trapped_water += max(0, right_max - height[right])
        
        # return trapped_water

        water = 0
        left, right = 0, len(height) - 1
        # left_max, right_max = 0, 0
        left_max, right_max = height[left], height[right]
        while left < right:
            cprint(f"left: {left}, right: {right}, left_max: {left_max}, right_max: {right_max}, water: {water}", "yellow")
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

            cprint(f"left: {left}, right: {right}, left_max: {left_max}, right_max: {right_max}, water: {water}", "cyan")

        return water
    


    
    def test(self):
        test_cases = [
            # ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
            # ([4,2,0,3,2,5], 9),
            # ([1], 0),
            # ([2,0], 0),
            # ([3,0,2], 2),
            ([5,5,1,7,1,1,5,2,7,6], 23)
        ]
        for height, expected in test_cases:
            cprint(f"height: {height}, expected: {expected}", "yellow")
            result = self.trap(height)
            try:
                assert result == expected
                cprint("Test passed", "green")
            except AssertionError:
                cprint(f"Test failed: got {result}", "red")
            print("-" * 50)

if __name__ == "__main__":
    solution = Solution()
    solution.test()