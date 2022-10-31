# 1st solution
# O(mn) time | O(1) space
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def check_diagonal(x, y):
            value = matrix[x][y]
            while x < m and y < n:
                if matrix[x][y] != value:
                    return False
                x += 1
                y += 1
            return True

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            x = i
            y = 0
            if not check_diagonal(x, y):
                return False
        
        for j in range(1, n):
            x = 0
            y = j
            if not check_diagonal(x, y):
                return False

        return True
