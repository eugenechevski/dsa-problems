"""
https://github.com/eugenechevski
https://leetcode.com/problems/find-all-anagrams-in-a-string
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        # A helper function for obtaining the index
        # of a character in the count map
        def index(char):
            return ord(char) - ord('a')

        # Build the count map of 'p'
        pCount = [0] * 26
        for ch in p:
            pCount[index(ch)] += 1

        # Build the count map of the first substring
        # of 's' which has the length of 'p'
        count = [0] * 26
        for i in range(len(p)):
            count[index(s[i])] += 1

        # Find all the indices where there's the anagram
        # by sliding the window and updating the count map
        res = []
        for i in range(len(s) - len(p) + 1):
            # Obtain the result
            if count == pCount:
                res.append(i)

            # Update the counts for the next iteration
            count[index(s[i])] -= 1
            count[index(s[(len(p) + i) % len(s)])] += 1

        return res
