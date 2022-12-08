"""
https://github.com/cherokee-rose
https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Constraints:
    * m == heights.length
    * n == heights[r].length
    * 1 <= m, n <= 200
    * 0 <= heights[r][c] <= 10^5
"""


class Solution:
    def pacificAtlantic(self, heights):
        # stores positions that can access an ocean
        atlantic = set()
        pacific = set()

        ROW, COL = len(heights), len(heights[0])  # Upper-boundary
        visits = pacific  # points to a current position-set

        def isValidPos(row, col):
            return (
                row >= 0 and row < ROW and
                col >= 0 and col < COL
            )

        def setPathAsTrue(row, col):
            if (row, col) in visits:
                return

            visits.add((row, col))

            if isValidPos(row, col + 1) and heights[row][col] <= heights[row][col + 1]:
                setPathAsTrue(row, col + 1)
            if isValidPos(row + 1, col) and heights[row][col] <= heights[row + 1][col]:
                setPathAsTrue(row + 1, col)
            if isValidPos(row, col - 1) and heights[row][col] <= heights[row][col - 1]:
                setPathAsTrue(row, col - 1)
            if isValidPos(row - 1, col) and heights[row][col] <= heights[row - 1][col]:
                setPathAsTrue(row - 1, col)

        for row in range(ROW):
            for col in range(COL):
                # Update the path for the pacific ocean
                if (
                    (row, col) not in pacific and
                    (row == 0 or col == 0)
                ):
                    visits = pacific
                    setPathAsTrue(row, col)

                # Update the path for the atlantic ocean
                if (
                    (row, col) not in atlantic and
                    (row == ROW - 1 or col == COL - 1)
                ):
                    visits = atlantic
                    setPathAsTrue(row, col)

        return list(pacific.intersection(atlantic))
