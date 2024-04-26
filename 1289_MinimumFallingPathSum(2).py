# 1st solution
# O(n^3) time | O(n^2) space
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp =[[float("inf") for _ in range(n)] for _ in range(n)]
        dp[0] = grid[0]
        for i in range(n - 1):
            for j in range(n):
                for k in range(n):
                    if j == k:
                        continue
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j] + grid[i+1][k])
        return min(dp[-1])
