"""
https://github.com/eugenechevski
https://leetcode.com/problems/shortest-bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 1
    
Example 2:
    Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
    Output: 2
    
Example 3:
    Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Output: 1
    
Constraints:
    * n == grid.length == grid[i].length
    * 2 <= n <= 100
    * grid[i][j] is either 0 or 1.
    * There are exactly two islands in grid.
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
            We need to find the shortest distance between two closest points on both islands that are
            adjacent to 0.

            Brute force approach:
                1. Find all point of both islands
                2. Find the shortest distance between each points
        """
        
        ROWS, COLS = len(grid), len(grid[0])

        island1 = set()
        island2 = set()

        currentIsland = island1
        visited = set()
        def dfs(row, col):
            nonlocal currentIsland, visited

            if (
                row < 0 or
                row == ROWS or
                col < 0 or
                col == COLS or
                (row, col) in visited or
                grid[row][col] == 0
            ):
                return

            visited.add((row, col))
            currentIsland.add((row, col))

            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)

        # Find all points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
                    currentIsland = island2
                
        # BFS
        q = deque(island1)
        steps = 0
        visited.clear()
        while q:
            levelLength = len(q)
            for _ in range(levelLength):
                island = q.popleft()
                
                # Move the bridge
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for d in directions:
                    nextIsland = (island[0] + d[0], island[1] + d[1])
                    
                    if nextIsland in island2:
                        return steps

                    if (
                        nextIsland[0] >= 0 and
                        nextIsland[0] < COLS and
                        nextIsland[1] >= 0 and
                        nextIsland[1] < ROWS and
                        nextIsland not in visited and
                        grid[nextIsland[0]][nextIsland[1]] == 0
                    ):
                        q.append(nextIsland)
                        visited.add(nextIsland)

            steps += 1

        return steps



