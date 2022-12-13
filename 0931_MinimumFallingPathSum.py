# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                left = float("inf") if j - 1 < 0 else matrix[i-1][j-1]
                middle = matrix[i-1][j]
                right = float("inf") if j + 1 >= n else matrix[i-1][j+1]
                matrix[i][j] += min(left, middle, right)
        return min(matrix[-1])