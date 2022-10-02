# 1st solution, top-down
# O(k * n * target) time | O(n * target) space
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        @cache
        def helper(m, t):
            if t <= 0:
                return 0
            if m == 1:
                if t <= k:
                    return 1
                else:
                    return 0
            ans = 0
            for i in range(1, k + 1):
                ans += helper(m - 1, t - i)
            ans %= MOD
            return ans
        return helper(n, target)

# 2nd solution, bottom-up
# O(k * n * target) time | O(target) space
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for _ in range(n):
            for num in reversed(range(target + 1)):
                dp[num] = 0
                for i in range(1, k + 1):
                    if num - i < 0:
                        break
                    dp[num] += dp[num - i]
                    dp[num] %= MOD
        return dp[target]