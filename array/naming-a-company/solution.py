"""
https://github.com/eugenechevski
https://leetcode.com/problems/naming-a-company
"""

from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Create groups
        groups = defaultdict(set)
        for idea in ideas:
            groups[idea[0]].add(idea[1:])

        result = 0
        groups = list(groups.values())
        for i in range(len(groups) - 1):
            first = groups[i]

            for j in range(i + 1, len(groups)):
                second = groups[j]

                intersect = 0
                for suff in first:
                    if suff in second:
                        intersect += 1

                distinct1 = len(first) - intersect
                distinct2 = len(second) - intersect
                result += distinct1 * distinct2

        return result * 2
