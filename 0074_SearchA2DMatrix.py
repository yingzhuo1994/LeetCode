# 1st solution
# O(log(m) + log(n)) time | O(1) space
# where m is the length of matrix, and n is the length of matrix[0]
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow, endRow = 0, len(matrix) - 1
        while startRow < endRow:
            middleRow = startRow + (endRow - startRow) // 2
            if matrix[middleRow][-1] > target:
                endRow = middleRow
            elif matrix[middleRow][-1] < target:
                startRow = middleRow + 1
            else:
                return True
        row = startRow
        startCol, endCol = 0, len(matrix[0]) - 1
        while startCol < endCol:
            middleCol = startCol + (endCol - startCol) // 2
            if matrix[row][middleCol] > target:
                endCol = middleCol
            elif matrix[row][middleCol] < target:
                startCol = middleCol + 1
            else:
                return True
        col = startCol
        return matrix[row][col] == target
