# 1st solution
# O(m * n * log(n)) time | O(n) space
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0
        
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j] else 0
                
        for i in range(m): 
            matrix[i].sort(reverse=True)
            for j in range(n):
                ans = max(ans, (j+1)*matrix[i][j])
        return ans