"""
https://github.com/eugenechevski
https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles
"""

from collections import defaultdict


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        freq = defaultdict(int)  # ratio: count

        # Count all the ratios
        for rect in rectangles:
            width, height = rect
            freq[width / height] += 1

        # Calculate the number of pairs the can be formed
        result = 0
        for count in freq.values():
            result += (count * (count - 1)) // 2

        return result
