# 1st solution, top-down
# O(k^n) time | O(k^n) space
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