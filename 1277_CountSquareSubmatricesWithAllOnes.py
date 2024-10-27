# 1st solution
# O(mn * min(m, n)) time | O(mn) space
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j]
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] += 1
        
        ans = 0
        for i in range(1, m + 1):
            for j in range(n + 1):
                k = min(i, j)
                for d in reversed(range(1, k + 1)):
                    ones = dp[i][j] - dp[i-d][j] - dp[i][j-d] + dp[i-d][j-d]
                    if ones == d * d:
                        ans += d
                        break
        return ans


# 2nd solution
# O(mn) time | O(mn) space
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans += f[i][j]
        return ans