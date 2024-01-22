"""
https://github.com/eugenechevski
https://leetcode.com/problems/optimal-partition-of-string
"""


class Solution:
    def partitionString(self, s: str) -> int:
        """
            Iterate through each character, adding to the current partition.
            Once a new character is already present in the current partition,
            increment the count and start the new partition with this new character.
        """

        res = 1
        curr = ''
        for c in s:
            if c in curr:
                res += 1
                curr = c
            else:
                curr += c

        return res
