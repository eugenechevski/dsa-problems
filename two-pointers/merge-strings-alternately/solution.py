"""
https://github.com/eugenechevski
https://leetcode.com/problems/merge-strings-alternately
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        l, r = 0, 0

        while l < len(word1) and r < len(word2):
            result += word1[l]
            result += word2[r]
            l += 1
            r += 1

        # Finish leftovers
        while l < len(word1):
            result += word1[l]
            l += 1
        while r < len(word2):
            result += word2[r]
            r += 1

        return result
