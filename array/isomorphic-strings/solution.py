"""
https://github.com/eugenechevski
https://leetcode.com/problems/isomorphic-strings
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {} # char of s -> char of t
        t_to_s = {} # char of t -> char of s

        for s1, t1 in zip(s, t):
            if (s1 in s_to_t and s_to_t[s1] != t1) or (t1 in t_to_s and t_to_s[t1] != s1):
                return False

            s_to_t[s1] = t1
            t_to_s[t1] = s1

        return True