"""
https://github.com/eugenechevski
https://leetcode.com/problems/burst-balloons
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)
        # dp[i][j] is the max number of coins in nums[i:j] range
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for offset in range(2, n):
            for i in range(n - offset):
                j = i + offset
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], balloons[i] * balloons[k] * balloons[j] +
                                   dp[i][k] + dp[k][j])

        return dp[0][n - 1]
