/*
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

*/

import assert from "node:assert";

function rotate(nums: number[], k: number): void {
    k = k % nums.length
    reverse(nums, 0, nums.length-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, nums.length-1)
}

function reverse(nums: number[], start: number, end: number): void {
    while (start < end){
        const temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start ++
        end --
    }
}

function test(){
    const testCases: [number[], number, number[]][] = [
        [[1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]],
        [[-1,-100,3,99], 2, [3,99,-1,-100]],
    ]
    for (const [nums, k, expected] of testCases){
        console.log('input: ', nums);
        console.log('k: ', k);
        console.log('expect: ', expected);
        rotate(nums, k)
        console.log('output: ', nums);
        try {
            assert.deepStrictEqual(nums, expected)
            console.log("Test passed")
        }catch (error){
            console.error("Test failed")
            console.error(error)
        }
    }
}
test()