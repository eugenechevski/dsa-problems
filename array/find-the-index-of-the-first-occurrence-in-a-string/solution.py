"""
https://github.com/eugenechevski
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
            KMP Algorithm
            Time complexity: O(n + m)
            Space complexity: O(n)
        """

        # Precompute the lookup table
        i, prevLPS = 1, 0
        lps = [0] * len(needle)
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                prevLPS += 1
                lps[i] = prevLPS
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        # Find the index of the first occurence
        i = 0  # haystack pointer
        j = 0  # needle pointer
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]

            # Found the index
            if j == len(needle):
                return i - len(needle)

        return - 1
