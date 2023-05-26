"""
https://github.com/eugenechevski
https://leetcode.com/problems/coin-change-ii
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount_plus_1 = amount + 1
        solutions = [0] * amount_plus_1
        solutions[0] = 1
        for coin in coins:
            for j in range(coin, amount_plus_1):
                solutions[j] += solutions[j - coin]
        return solutions[-1]
