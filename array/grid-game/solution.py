"""
https://github.com/eugenechevski
https://leetcode.com/problems/grid-game
"""

class Solution(object):
    def gridGame(self, grid):
        """
            The idea is to minimize the maximums.
            We can keep track of either top or bottom prefixes for the second robot.
        """
        result = float("inf")
        bottom, top = 0, sum(grid[0])

        for a, b in zip(grid[0], grid[1]):
            top -= a
            result = min(result, max(bottom, top))
            bottom += b
        return result

        