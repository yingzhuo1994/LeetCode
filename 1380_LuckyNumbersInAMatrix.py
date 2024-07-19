# 1st solution
# O(mn) time | O(m + n) space
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        minRow = [min(row) for row in matrix]
        maxCol = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == minRow[i] and matrix[i][j] == maxCol[j]:
                    ans.append(matrix[i][j])
        return ans