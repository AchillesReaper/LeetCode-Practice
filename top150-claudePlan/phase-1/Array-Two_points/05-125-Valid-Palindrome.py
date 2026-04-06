'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

from termcolor import cprint

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        if n < 2:
            return True
        
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False
        return True
    
    def test(self):
        test_cases = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True)
        ]
        for s, expected in test_cases:
            cprint(f"s: '{s}', expected: {expected}", "yellow")
            result = self.isPalindrome(s)
            try:
                assert result == expected
                cprint("Passed", "green")
            except AssertionError:
                cprint(f"Failed: expected {expected}, got {result}", "red")
            print("-" * 50)


if __name__ == "__main__":
    Solution().test()