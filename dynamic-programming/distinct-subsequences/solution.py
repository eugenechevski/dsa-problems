"""
https://github.com/eugenechevski
https://leetcode.com/problems/distinct-subsequences
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
            At each point, we either take or skip a letter in s
        """
        # Initialize a 2D dp array with dimensions (len(s)+1) x (len(t)+1)
        # The value dp[i][j] represents the number of distinct subsequences of the first i characters of s 
        # that equals the first j characters of t.
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        # Base case: If t is an empty string, there's always one way to form it 
        # by deleting all characters from s.
        for i in range(len(s) + 1):
            dp[i][0] = 1
    
        # Populate the dp array using the transition function
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # If the current character in s matches the current character in t
                if s[i-1] == t[j-1]:
                    # We can either exclude the current character of s or include it
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    # We can only exclude the current character of s
                    dp[i][j] = dp[i-1][j]
    
        # The final answer is stored in dp[len(s)][len(t)]
        return dp[len(s)][len(t)]