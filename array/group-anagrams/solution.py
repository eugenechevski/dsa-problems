"""
https://leetcode.com/problems/group-anagrams/
https://github.com/eugenechevski
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # sorted string: all strings with the same characters
        
        for word in strs:
            # find the key of a group to which the word belongs
            sorted_word = ''.join(sorted(word))
            
            if not sorted_word in groups:
                groups[sorted_word] = []

            groups[sorted_word].append(word)

        return groups.values()