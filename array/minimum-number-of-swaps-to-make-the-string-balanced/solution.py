"""
https://github.com/eugenechevski
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        """
            Iterate from the beginning and swap when # of closing brackets exceeds
            the # of opening brackets.
        """

        left, right = 0, len(s) - 1
        result = 0
        openCount, closeCount = 0, 0
        while left < right:
            if s[left] == '[':
                openCount += 1
            else:
                closeCount += 1

            # Make the swap
            if openCount < closeCount and s[left] == ']':
                # Find the first open bracket from the end
                while left < right and s[right] != '[':
                    right -= 1

                # Swap
                if left < right:
                    result += 1
                    openCount += 1
                    closeCount -= 1

            left += 1

        return result
