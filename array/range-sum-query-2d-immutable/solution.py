"""
https://github.com/eugenechevski
https://leetcode.com/problems/range-sum-query-2d-immutable
"""


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefix = [[0 for _ in range(self.n)] for _ in range(self.m)]

        # Add horizontal prefixes
        for r in range(self.m):
            for c in range(self.n):
                if c == 0:
                    self.prefix[r][c] = matrix[r][c]
                else:
                    self.prefix[r][c] = self.prefix[r][c - 1] + matrix[r][c]

        # Add vertical prefixes
        for c in range(self.n):
            for r in range(self.m):
                if r > 0:
                    self.prefix[r][c] += self.prefix[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix[row2][col2]

        # Subtract the extra parts
        # the extra parts are located on the left
        # and on the top of the current region
        # Also, we need to be careful not oversubtract the overlapping part
        # of (row - 1, col - 1) coordinates.
        if col1 - 1 >= 0:
            result -= self.prefix[row2][col1 - 1]
        if row1 - 1 >= 0:
            result -= self.prefix[row1 - 1][col2]

        # Add the overlapping part back
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            result += self.prefix[row1 - 1][col1 - 1]

        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
