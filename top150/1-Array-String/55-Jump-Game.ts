/*
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
*/

import assert from 'node:assert';
function canJump(nums: number[]): boolean {
    let maxReachable = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > maxReachable) {
            return false; // If we can't reach this index, return false
        }else{
            maxReachable = Math.max(maxReachable, i + nums[i]); // Update the maximum reachable index
            if (maxReachable >= nums.length - 1) {
                return true; // If we can reach or exceed the last index, return true
            }
        }
    }
    return false;
};

function test() {
    const testCases: [number[], boolean][] = [
        [[2,3,1,1,4], true],
        [[3,2,1,0,4], false],
    ];

    for (const [nums, expected] of testCases) {
        console.log("nums: ", nums, "expected: ", expected);
        const result = canJump(nums);
        console.log('output:', result);
        try {
            assert.strictEqual(result, expected);
            console.log('Test passed!');
        } catch (error) {
            console.error('Test failed:');
        }
        console.log('='.repeat(50));
    }
}

test();