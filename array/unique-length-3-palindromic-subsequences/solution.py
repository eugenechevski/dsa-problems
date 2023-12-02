"""
https://github.com/eugenechevski
https://leetcode.com/problems/unique-length-3-palindromic-subsequences
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        uniqueChars = set(s)
        for char in uniqueChars:
            first, last = s.find(char), s.rfind(char)
            count += len(set(s[first + 1: last]))

        return count
