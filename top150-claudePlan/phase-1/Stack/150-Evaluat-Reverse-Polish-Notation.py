'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

from typing import List
from termcolor import cprint


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            if e in '+-*/':
                b = stack.pop()
                a = stack.pop()
                match e:
                    case '+':
                        stack.append(a+b)
                    case '-':
                        stack.append(a-b)
                    case '*':
                        stack.append(a*b)
                    case '/':
                        stack.append(int(a/b))
                    case _:
                        raise ValueError(f'{e} is not a valid token')
            else:
                stack.append(int(e))
            # cprint(f"Current stack: {stack}", 'white', "on_blue")
        cprint(f"Final stack: {stack}", 'white', "on_cyan")
        return stack[0]


test_cases = [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    (["3", "4", "+"], 7),
    (["5", "1", "2", "+", "4", "*", "+", "3", "-"], 14)
]

def test():
    for tokens, expected in test_cases:
        cprint(f"Testing with tokens: {tokens}", 'yellow')
        result = Solution().evalRPN(tokens)
        cprint(f"Expected: {expected}, Got: {result}", 'blue')
        if result == expected:
            cprint("Passed!", 'green')
        else:
            cprint("Failed!", 'red')

if __name__ == "__main__":
    test()