'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

from collections import Counter
from typing import List

from termcolor import cprint

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = len(s) + 1
        need    = Counter(t)
        window  = Counter()
        start, left, valid = 0, 0, 0

        for right in range(len(s)):
            char = s[right]

            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    valid += 1
                
            while valid == len(need):
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1
                
                char = s[left]
                window[char] -= 1
                if char in need and window[char] < need[char]:
                    valid -= 1
                left += 1

        
        
        return "" if min_len == len(s) + 1 else s[start:start+min_len]
    

    def test(self):
        test_cases = [
            ("ADOBECODEBANC", "ABC", "BANC"),
            ("a", "a", "a"),
            ("a", "aa", ""),
        ]
        for s, t, expected in test_cases:
            cprint(f"Testing with s: '{s}', t: '{t}'", 'yellow')
            
            result = self.minWindow(s, t)
            cprint(f"Expected: '{expected}', Got: '{result}'", 'yellow')
            if result == expected:
                cprint("PASS", 'green')
            else:
                cprint("FAIL", 'red')
            print('-'*50)

if __name__ == "__main__":
    Solution().test()