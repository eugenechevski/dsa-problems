"""
https://github.com/eugenechevski
https://leetcode.com/problems/check-if-move-is-legal

You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. 
On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.
Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). 
However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).
A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). 
You can find examples for good lines in the figure below:

Given two integers rMove and cMove and a character color representing the color you are playing as (white or black), 
return true if changing cell (rMove, cMove) to color color is a legal move, or false if it is not legal.

Example 1:
    Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
    Output: true
    Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
    The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.

Example 2:
    Input: board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
    Output: false
    Explanation: While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.

Constraints:
    * board.length == board[r].length == 8
    * 0 <= rMove, cMove < 8
    * board[rMove][cMove] == '.'
    * color is either 'B' or 'W'.
"""


class Solution:
    def checkMove(self, board, rMove, cMove, color):
        ROWS, COLS = len(board), len(board[0])
        oppositeColor = 'W' if color == 'B' else 'B'

        def isLegalMove(row, col):
            distanceX = abs(cMove - col)
            distanceY = abs(rMove - row)

            if (
                board[row][col] == '.' or
                (board[row][col] == color and (
                    (distanceX == 1 and distanceY == 0) or
                    (distanceY == 1 and distanceX == 0) or
                    (distanceX == 1 and distanceY == 1)
                ))
            ):
                return False

            return True

        def iterate(start, end, step, coord):
            row, col = 0, 0
            for i in range(start, end, step):
                if coord == 'row':
                    row = i
                    col = cMove
                elif coord == 'col':
                    row = rMove
                    col = i
                elif coord == 'row+col+':
                    row = rMove + i
                    col = cMove + i
                elif coord == 'row-col+':
                    row = rMove - i
                    col = cMove + i
                elif coord == 'row+col-':
                    row = rMove + i
                    col = cMove - i
                elif coord == 'row-col-':
                    row = rMove - i
                    col = cMove - i

                cellColor = board[row][col]

                if cellColor == oppositeColor:
                    continue
                elif isLegalMove(row, col):
                    break
                else:
                    return False

            return True

        def isValidHorizontal():
            def isValidToLeft():
                return iterate(cMove - 1, -1, -1, 'col')

            def isValidToRight():
                return iterate(cMove + 1, COLS, 1, 'col')

            return isValidToLeft() or isValidToRight()

        def isValidVertical():
            def isValidUp():
                return iterate(rMove - 1, -1, -1, 'row')

            def isValidDown():
                return iterate(rMove + 1, ROWS, 1, 'row')

            return isValidUp() or isValidDown()

        def isValidDiagonal():
            def isValidRightAndDown():
                return iterate(1, min(ROWS - rMove, COLS - cMove), 1, 'row+col+')

            def isValidRightAndUp():
                return iterate(1, min(rMove + 1, COLS - cMove), 1, 'row-col+')

            def isValidLeftAndUp():
                return iterate(1, min(rMove + 1, cMove + 1), 1, 'row-col-')

            def isValidLeftAndDown():
                return iterate(1, min(ROWS - rMove, cMove + 1), 1, 'row+col-')

            return (
                isValidRightAndDown() or
                isValidRightAndUp() or
                isValidLeftAndUp() or
                isValidLeftAndDown()
            )

        return (
            isValidHorizontal() or
            isValidVertical() or
            isValidDiagonal()
        )
