'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''
from typing import List
from termcolor import cprint
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums)
        left, right = 0, 0
        cumm = nums[0]
        while left <= right and right < len(nums):
            print(f"left: {left}, right: {right}, cumm: {cumm}, min_len: {min_len}")
            if cumm >= target:
                min_len = min(min_len, right-left +1)
                if min_len == 1: 
                    cprint(f"min_len is 1, returning {min_len}", 'blue')
                    return min_len
                if right == len(nums)-1:
                    cprint(f"right is at the end of the array, returning {min_len}", 'blue')
                    return min_len
                cumm -= nums[left]
                left += 1
            else:
                right += 1
                cumm += nums[right] if right < len(nums) else 0

        if min_len == len(nums) and cumm < target:
            return 0
        else:
            return min_len
        
    def test(self):
        test_cases = [
            (15, [1,2,3,4,5], 5),
            # (7, [2,3,1,2,4,3], 2),
            # (4, [1,4,4], 1),
            # (11, [1,1,1,1,1,1,1,1], 0)
        ]
        for target, nums, expected in test_cases:
            cprint(f"target: {target}, nums: {nums}, expected: {expected}", 'yellow')
            result = self.minSubArrayLen(target, nums)
            cprint(f"result: {result}", 'yellow')
            if result == expected:
                cprint("PASS", 'green')
            else:
                cprint("FAIL", 'red')
            print('-'*50)

if __name__ == "__main__":
    Solution().test()
