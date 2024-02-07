"""
https://github.com/eugenechevski
https://leetcode.com/problems/valid-palindrome-ii
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        skipped = False

        while l < r:
            if s[l] != s[r]:
                self.s = s
                return self.isPal(l + 1, r) or self.isPal(l, r - 1)
            l += 1
            r -= 1

        return True

    def isPal(self, l, r):
        s = self.s

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
