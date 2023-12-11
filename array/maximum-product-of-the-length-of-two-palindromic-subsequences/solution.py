"""
https://github.com/eugenechevski
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences
"""

class Solution:
    def maxProduct(self, s: str) -> int:
        masks = [] # masks for subsequences
        subs = [] # corresponding subsequences
        palSubs = [] # palindromic subsequences

        # Generate all possible subsequences
        for i in range(len(s) - 1, -1, -1):
            length = len(masks)

            for j in range(length):
                # Add the current character to the subsequence
                sub = subs[j] + s[len(s) - i - 1]
                # Update the mask to include the current character
                mask = masks[j] | 1 << i

                # If the subsequence is a palindrome, add it to the list of palindromic subsequences
                if self.isPalindrom(sub):
                    palSubs.append((sub, mask))

                # Add the subsequence and its mask to the lists
                subs.append(sub)
                masks.append(mask)

            # Add the current character as a single-character subsequence
            palSubs.append((s[len(s) - i - 1], 1 << i))
            masks.append(1 << i)
            subs.append(s[len(s) - i - 1])

        result = 1
        # Iterate over all pairs of palindromic subsequences
        for i in range(len(palSubs)):
            sub1, mask1 = palSubs[i]

            for j in range(len(palSubs)):
                if i == j:
                    continue
                sub2, mask2 = palSubs[j]
                # If the subsequences have no overlap, calculate the product of their lengths
                if mask1 & mask2 == 0: # no overlap
                    result = max(result, len(sub1) * len(sub2))

        return result

    def isPalindrom(self, _str):
        left, right = 0, len(_str) - 1
        result = True
        # Check if the string is a palindrome
        while left < right:
            if _str[left] != _str[right]:
                result = False
                break
            left += 1
            right -= 1

        return result
