"""
https://github.com/eugenechevski
https://leetcode.com/problems/longest-common-prefix
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = {}  # prefix: count

        # Build the prefixes
        for word in strs:
            prefix = ''
            for char in word:
                prefix += char

                if not prefix in prefixes:
                    prefixes[prefix] = 0

                prefixes[prefix] += 1

        # Find the longest common prefix
        longest = ''
        max_len = 0
        for prefix, count in prefixes.items():
            if count >= max_len:
                longest = prefix
                max_len = count

        return longest if max_len == len(strs) else ''
