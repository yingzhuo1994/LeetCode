# 1st solution
# O(s * min(s, n)) time | O(s * min(s, n))
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        limit = min(steps, arrLen)
        dp = [[0 for _ in range(limit)] for _ in range(steps + 1)]
        dp[0][0] = 1
        for step in range(steps):
            for i in range(limit):
                if i > 0:
                    dp[step + 1][i - 1] += dp[step][i]
                dp[step + 1][i] += dp[step][i]
                if i < limit - 1:
                    dp[step + 1][i + 1] += dp[step][i]
            
        MOD = 10**9 + 7
        return dp[-1][0] % MOD