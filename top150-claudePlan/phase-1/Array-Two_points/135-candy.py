from termcolor import cprint
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # checking from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] += max
            cprint(f"i: {i}, candies: {candies}", 'white', "on_yellow")
        
        # checking from right to left
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candies[j] = max(candies[j], candies[j+1] + 1)
            cprint(f"j: {j}, candies: {candies}", 'white', "on_blue")
        return sum(candies)

ratings = [1,2,87,87,87,2,1]
solution = Solution()
cprint(solution.candy(ratings), 'green')