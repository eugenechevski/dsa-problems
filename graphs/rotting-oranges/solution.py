"""
https://github.com/eugenechevski
https://leetcode.com/problems/rotting-oranges

You are given an m x n grid where each cell can have one of three values:
    * 0 representing an empty cell,
    * 1 representing a fresh orange, or
    * 2 representing a rotten orange.
    
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 10
    * grid[i][j] is 0, 1, or 2.
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(rottens, fresh_count):
            nonlocal visited

            minutes = -1 if len(rottens) > 0 or fresh_count > 0 else 0
            q = deque(rottens)
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            while q:
                q_len = len(q)
                for _ in range(q_len):
                    r, c = q.popleft()
                    # Make all neighboring oranges rotten
                    for d in directions:
                        pos = (r + d[0], c + d[1])
                        if (
                            pos[0] >= 0 and pos[0] < ROWS and
                            pos[1] >= 0 and pos[1] < COLS and
                            pos not in visited and
                            grid[pos[0]][pos[1]] == 1
                        ):
                            fresh_count -= 1
                            grid[pos[0]][pos[1]] = 2
                            visited.add(pos)
                            q.append(pos)

                minutes += 1

            return minutes if fresh_count == 0 else -1

        # Find all initial rotten oranges
        rottens = []
        fresh_count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rottens.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        return bfs(rottens, fresh_count)
