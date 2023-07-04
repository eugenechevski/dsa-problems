"""
https://github.com/eugenechevski
https://leetcode.com/problems/interleaving-string
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            Decision-Tree Approach
        """

        len_1 = len(s1)
        len_2 = len(s2)
        len_3 = len(s3)

        if len_1 + len_2 != len_3:
            return False

        visited = set()

        def dfs(i, j, k):
            if k == len_3:
                return True

            if (
                (i, j, k) in visited or
                i < len_1 and j < len_2 and s1[i] != s3[k] and s2[j] != s3[k] or
                i == len_1 and j < len_2 and s2[j] != s3[k] or
                j == len_2 and i < len_1 and s1[i] != s3[k]
            ):
                return False

            visited.add((i, j, k))

            return (
                i < len_1 and s1[i] == s3[k] and dfs(i + 1, j, k + 1) or
                j < len_2 and s2[j] == s3[k] and dfs(i, j + 1, k + 1)
            )

        return dfs(0, 0, 0)