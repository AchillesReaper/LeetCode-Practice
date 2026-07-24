'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
from termcolor import cprint
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = left = 0
        max_len = 0
        seen = {}

        for right in range(len(s)):
            char = s[right]
            if char in seen and left <= seen[char]:
                left = seen[char] + 1
            seen[char] = right
            max_len = max(max_len, right-left+1)
        
        return max_len
    
    def test(self):
        test_cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            (" ", 1),
            ("au", 2),
            ("dvdf", 3)
        ]
        for s, expected in test_cases:
            cprint(f"Testing with s: '{s}'", 'yellow')
            result = self.lengthOfLongestSubstring(s)
            cprint(f"Expected: {expected}, Got: {result}", 'blue')
            if result == expected:
                cprint("Passed!", 'green')
            else:
                cprint("Failed!", 'red')
            print('-'*50)


if __name__ == "__main__":
    Solution().test()
    