"""
https://github.com/eugenechevski
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
"""

from math import pow


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        curr = 0
        for i in range(k):
            curr |= int(s[i]) << i

        uniqs = set([curr])
        for i in range(1, len(s) - k + 1):
            # slide the window
            curr >>= 1
            # move it to the k-th position in our window
            curr |= int(s[i + k - 1]) << (k - 1)
            uniqs.add(curr)

        return len(uniqs) == pow(2, k)
