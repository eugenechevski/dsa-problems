"""
https://github.com/cherokee-rose
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example 1:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Example 2:
    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []

Constraints:
    * m == board.length
    * n == board[i].length
    * 1 <= m, n <= 12
    * board[i][j] is a lowercase English letter.
    * 1 <= words.length <= 3 * 10^4
    * 1 <= words[i].length <= 10
    * words[i] consists of lowercase English letters.
    * All the strings of words are unique.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.refs = 0  # number of nodes that the node leads to

    def addWord(self, word):
        current = self
        current.refs += 1

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.refs += 1
        current.is_end = True

    def removeWord(self, word):
        current = self
        current.refs -= 1

        for char in word:
            if char in current.children:
                current = current.children[char]
                current.refs -= 1


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Initialize the Trie with the given words
        for word in words:
            root.addWord(word)

        ROW, COL = len(board), len(board[0])
        visited, results = set(), set()

        def dfs(row, col, node, word):
            if (
                row < 0 or
                col < 0 or
                row == ROW or
                col == COL or
                board[row][col] not in node.children or
                node.children[board[row][col]].refs < 1 or
                (row, col) in visited
            ):
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.is_end:
                node.is_end = False
                results.add(word)
                root.removeWord(word)

            dfs(row, col + 1, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row - 1, col, node, word)

            visited.remove((row, col))

        for row in range(ROW):
            for col in range(COL):
                dfs(row, col, root, "")

        return list(results)