'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

from termcolor import cprint
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return result
    
    def threeSum_sub(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                k_sum = nums[i] + nums[left] + nums[right]
                match k_sum:
                    case x if x < 0:
                        left += 1
                    case x if x > 0:
                        right -= 1
                    case 0:
                        answer.append([nums[i], nums[left], nums[right]])
                        while left > right and nums[left] == nums[left+1]:
                            left += 1
                        while left > right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        
        return answer
    
    def test(self):
        test_cases = [
            ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
            ([0,1,1], []),
            ([0,0,0], [[0,0,0]]),
            ([-2,0,0,2,2], [[-2,0,2]])
        ]
        for nums, expected in test_cases:
            cprint(f"nums: {nums}, expected: {expected}", "yellow")
            result = self.threeSum(nums)
            try:
                assert sorted(result) == sorted(expected)
                cprint("Test passed!", "green")
            except AssertionError:
                cprint(f"Test failed! Got: {result}", "red")
            print("-" * 50)

if __name__ == "__main__":
    Solution().test()