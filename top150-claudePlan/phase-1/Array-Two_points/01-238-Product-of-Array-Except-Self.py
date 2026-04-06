'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

-----------------------
Approach: Prefix & Suffix Products
For each index i, answer[i] = product of everything left of i × product of everything right of i.

Two passes, O(1) extra space:

Left pass: accumulate prefix product into answer
Right pass: multiply each entry by a running suffix product

nums =    [1,   2,   3,   4]
prefix =  [1,   1,   2,   6]   ← product of elements before i
suffix =  [24,  12,  4,   1]   ← product of elements after i
answer =  [24,  12,  8,   6]   ← prefix[i] * suffix[i]

'''

from termcolor import cprint

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer
    
    def test(self):
        test_cases = [
            ([1,2,3,4], [24,12,8,6]),
            ([-1,1,0,-3,3], [0,0,9,0,0]),
        ]
        for nums, expected in test_cases:
            cprint(f"Testing with input: {nums}")
            output = self.productExceptSelf(nums)
            cprint(f"Expected output: {expected}, Actual output: {output}")
            try:
                assert output == expected
                cprint("Test passed!", color="green")
            except AssertionError:
                cprint("Test failed!", color="red")

            print("-" * 50)

if __name__ == "__main__":
    solution = Solution()
    solution.test()
