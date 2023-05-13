# 1st solution
# O(n) time | O(n) space 
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(high + 1):
            if i + zero <= high:
                dp[i+zero] += dp[i]
            if i + one <= high:
                dp[i+one] += dp[i]
        return sum(dp[low:high+1] + [0]) % MOD