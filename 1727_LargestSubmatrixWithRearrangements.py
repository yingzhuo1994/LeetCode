# 1st solution
# O(m * n * log(n)) time | O(n) space
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0
        
        for j in range(n):
            for i in range(1, m):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
                
        for row in matrix: 
            row.sort(reverse=True)
            for j, height in enumerate(row, 1):
                ans = max(ans, j * height)
        return ans