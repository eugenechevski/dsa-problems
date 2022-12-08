"""
https://github.com/cherokee-rose
https://leetcode.com/problems/max-area-of-island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 50
    * grid[i][j] is either 0 or 1.
"""

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            nonlocal visited

            area = 1
            q = deque([(row, col)])
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            visited.add((row, col))

            while q:
                pos = q.popleft()
                for d in directions:
                    r, c = pos[0] + d[0], pos[1] + d[1]
                    if (
                        r >= 0 and
                        r < ROW and
                        c >= 0 and
                        c < COL and
                        grid[r][c] == 1 and
                        (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1

            return area

        max_area = 0

        for row in range(ROW):
            for col in range(COL):
                if (
                    (row, col) not in visited and
                    grid[row][col] == 1
                ):
                    max_area = max(max_area, bfs(row, col))

        return max_area
