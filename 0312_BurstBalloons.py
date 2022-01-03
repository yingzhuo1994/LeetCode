# 1st solution
# O(n^3) time | O(n^2) space
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins, n = [1] + nums + [1], len(nums) + 2
        dp = [[0] * n for _ in range(n)]
        
        for i in reversed(range(n - 1)):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], coins[i]*coins[k]*coins[j] + dp[i][k] + dp[k][j])
        
        return dp[0][n-1]