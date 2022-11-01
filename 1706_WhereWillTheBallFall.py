# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if grid[-1][j] > 0:
                if j + 1 < n and grid[-1][j + 1] > 0:
                    dp[-1][j] = j + 1
            else:
                if j > 0 and grid[-1][j - 1] < 0:
                    dp[-1][j] = j - 1

        for i in reversed(range(m - 1)):
            for j in range(n):
                if grid[i][j] > 0:
                    if j + 1 < n and grid[i][j + 1] > 0:
                        dp[i][j] = dp[i + 1][j + 1]
                else:
                    if j > 0 and grid[i][j - 1] < 0:
                        dp[i][j] = dp[i + 1][j - 1]
        
        return dp[0]
