# O(M) time | O(1) space
# M is the number of cells in the matrix.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                self.elementsRotate(matrix, i, j)

    def elementsRotate(self, matrix, x, y):
        # x is the row number, and y is column nummber
        n = len(matrix)
        matrix[x][y], matrix[y][n-1-x], matrix[n-1-x][n-1-y], matrix[n-1-y][x] =\
        matrix[n-1-y][x], matrix[x][y], matrix[y][n-1-x], matrix[n-1-x][n-1-y]
