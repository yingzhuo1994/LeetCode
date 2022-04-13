# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for _ in range(n)]
        startRow, startCol = 0, 0
        endRow, endCol = n - 1, n - 1
        state = (0, 1)
        num = 1
        i, j = 0, 0
        while startRow <= i <= endRow and startCol <= j <= endCol:
            matrix[i][j] = num
            num += 1
            if state == (0, 1):
                if j == endCol:
                    i += 1
                    startRow += 1
                    state = (1, 0)
                else:
                    j += 1
            elif state == (1, 0):
                if i == endRow:
                    j -= 1
                    endCol -= 1
                    state = (0, -1)
                else:
                    i += 1
            elif state == (0, -1):
                if j == startCol:
                    i -= 1
                    endRow -= 1
                    state = (-1, 0)
                else:
                    j -= 1
            elif state == (-1, 0):
                if i == startRow:
                    j += 1
                    startCol += 1
                    state = (0, 1)
                else:
                    i -= 1
        return matrix
