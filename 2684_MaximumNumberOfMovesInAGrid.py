# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n - 1):
            for i in range(m):
                if j > 0 and dp[i][j] == 0:
                    continue
                if i > 0 and grid[i-1][j+1] > grid[i][j]:
                    dp[i-1][j+1] = max(dp[i-1][j+1], dp[i][j] + 1)
                if grid[i][j+1] > grid[i][j]:
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j] + 1)
                if i + 1 < m and grid[i+1][j+1] > grid[i][j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
        return max(map(max, dp))