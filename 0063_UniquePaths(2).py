# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        