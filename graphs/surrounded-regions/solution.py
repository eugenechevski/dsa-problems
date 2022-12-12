"""
https://github.com/cherokee-rose
https://leetcode.com/problems/surrounded-regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Explanation: Notice that an 'O' should not be flipped if:
    - It is on the border, or
    - It is adjacent to an 'O' that should not be flipped.
    The bottom 'O' is on the border, so it is not flipped.
    The other three 'O' form a surrounded region, so they are flipped.

Example 2:
    Input: board = [["X"]]
    Output: [["X"]]

Constraints:
    * m == board.length
    * n == board[i].length
    * 1 <= m, n <= 200
    * board[i][j] is 'X' or 'O'.
"""

from collections import deque

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        invalid = set()
        ROWS, COLS = len(board), len(board[0])

        def bfs(row, col):
            nonlocal invalid

            if (
                (row, col) in invalid or
                row == 0 or
                row == ROWS - 1 or
                col == 0 or
                col == COLS - 1
            ):
                return [[(row, col)], False]

            visited = set([(row, col)])
            q = deque([(row, col)])
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            while q:
                r, c = q.popleft()

                for d in directions:
                    neighbor = (r + d[0], c + d[1])

                    if (
                        board[neighbor[0]][neighbor[1]] == 'O' and
                        (neighbor in invalid or
                         neighbor[0] == 0 or
                         neighbor[0] == ROWS - 1 or
                         neighbor[1] == 0 or
                         neighbor[1] == COLS - 1)
                    ):
                        visited.add(neighbor)
                        return [list(visited), False]

                    if (
                        neighbor not in visited and
                        board[neighbor[0]][neighbor[1]] == 'O'
                    ):
                        visited.add(neighbor)
                        q.append(neighbor)

            return [list(visited), True]

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    visited, captured = bfs(row, col)
                    for r, c in visited:
                        if captured:
                            board[r][c] = 'X'
                        else:
                            invalid.add((r, c))
