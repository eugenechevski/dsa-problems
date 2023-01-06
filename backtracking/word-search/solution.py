"""
https://github.com/eugenechevski
https://leetcode.com/problems/word-search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once. 

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true
    
Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false

Constraints:
    * m == board.length
    * n = board[i].length
    * 1 <= m, n <= 6
    * 1 <= word.length <= 15
    * board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def backtrack(row, col, cur_word):
            if cur_word == '':
                return True

            if (
               row < 0 or
               row == ROW or
               col < 0 or
               col == COL or
               (row, col) in visited or
               board[row][col] != cur_word[0]
               ):
                return False

            visited.add((row, col))
            result = (
                backtrack(row, col + 1, cur_word[1:]) or
                backtrack(row + 1, col, cur_word[1:]) or
                backtrack(row, col - 1, cur_word[1:]) or
                backtrack(row - 1, col, cur_word[1:])
            )
            visited.remove((row, col))

            return result

        for row in range(ROW):
            for col in range(COL):
                if backtrack(row, col, word):
                    return True

        return False
