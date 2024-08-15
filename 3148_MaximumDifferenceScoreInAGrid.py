# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + grid[i][j] - grid[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + grid[i][j] - grid[i][j-1])
                    
        ans = max(max(row) for row in dp)
        if ans > 0:
            return ans
        
        diff = float("-inf")
        for i in range(m):
            for j in range(n):
                if i > 0:
                    diff = max(diff, grid[i][j] - grid[i-1][j])
                if j > 0:
                    diff = max(diff, grid[i][j] - grid[i][j-1])
        return diff