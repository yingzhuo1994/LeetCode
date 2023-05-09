# 1st solution
# O(n) time | O(n) space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst = []
        startRow, endRow = 0, len(matrix) - 1
        startColumn, endColumn = 0, len(matrix[0]) - 1
        place = (0, 0)
        while startRow <= endRow and startColumn <= endColumn:
            if place == (0, 0):
                for j in range(startColumn, endColumn + 1):
                    lst.append(matrix[startRow][j])
                startRow += 1
                place = (0, -1)
            elif place == (0, -1):
                for i in range(startRow, endRow + 1):
                    lst.append(matrix[i][endColumn])
                endColumn -= 1
                place = (-1, -1)
            elif place == (-1, -1):
                for j in reversed(range(startColumn, endColumn + 1)):
                    lst.append(matrix[endRow][j])
                endRow -= 1
                place = (-1, 0)
            elif place == (-1, 0):
                for i in reversed(range(startRow, endRow + 1)):
                    lst.append(matrix[i][startColumn])
                startColumn += 1
                place = (0, 0)
        return lst
