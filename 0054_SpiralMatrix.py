# 1st solution
# O(mn) time | O(mn) space
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

# 2nd solution
# O(mn) time | O(mn) space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix[0]), len(matrix)
        x, y, dx, dy = 0, 0, 1, 0
        ans = []
        for _ in range(m*n):
            if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] == "*":
                dx, dy = -dy, dx
                
            ans.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x + dx, y + dy
        
        return ans