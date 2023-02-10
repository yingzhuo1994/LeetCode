# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:        
        n = len(grid)
        land_count = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    land_count += 1
        if land_count == 0 or land_count == n * n:
            return -1
        
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i > 0:
                    top = dp[i-1][j]
                    dp[i][j] = min(dp[i][j], top + 1)
                if j > 0:
                    left = dp[i][j - 1]
                    dp[i][j] = min(dp[i][j], left + 1)

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if grid[i][j] == 1:
                    continue
                if i < n - 1:
                    bottom = dp[i+1][j]
                    dp[i][j] = min(dp[i][j], bottom + 1)
                if j < n - 1:
                    right = dp[i][j + 1]
                    dp[i][j] = min(dp[i][j], right + 1)
        
        ans = 1
        for i in range(n):
            for j in range(n):
                ans = max(ans, dp[i][j])
        return ans

        
        
