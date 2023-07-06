"""
https://github.com/eugenechevski
https://leetcode.com/problems/longest-increasing-path-in-a-matrix
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # A dictionary to store the longest increasing path (LIP) length starting from each cell
        visited = {}
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        # A set to store the cells in the current path
        path = set()

        # A helper function to check if a move is valid
        def isValidMove(row, col):
            # Check if the cell is within the matrix boundaries
            return 0 <= row < m and 0 <= col < n

        # A helper function to get all valid moves from a cell
        def getValidMoves(row, col):
            moves = []
            # Define the four possible directions to move
            paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for path in paths:
                d_row, d_col = path
                new_row, new_col = row + d_row, col + d_col
                # Check if the move is valid and the new cell value is greater than the current cell value
                if isValidMove(new_row, new_col) and matrix[row][col] < matrix[new_row][new_col]:
                    moves.append((new_row, new_col))

            return moves

        # A helper function to perform depth-first search (DFS) from a cell
        def dfs(row, col):
            nonlocal visited, m, n

            # If the cell has been visited, return the stored LIP length
            if (row, col) in visited:
                return visited[(row, col)]

            # If the cell is in the current path, return 0 to avoid cycles
            if (row, col) in path:
                return 0

            # Add the cell to the current path
            path.add((row, col))
            # Get all valid moves from the cell
            validMoves = getValidMoves(row, col)
            max_lip = 0
            # Perform DFS from each valid move and update the maximum LIP length
            for move in validMoves:
                v_row, v_col = move
                max_lip = max(max_lip, dfs(v_row, v_col))

            # Store the LIP length starting from the cell and remove the cell from the current path
            visited[(row, col)] = 1 + max_lip
            path.remove((row, col))

            return visited[(row, col)]

        # Initialize the maximum LIP length
        LIP = 0
        # Perform DFS from each cell in the matrix and update the maximum LIP length
        for row in range(m):
            for col in range(n):
                dfs(row, col)
                LIP = max(LIP, visited[(row, col)])

        # Return the maximum LIP length
        return LIP
