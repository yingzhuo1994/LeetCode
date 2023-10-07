# 1st solution, Top-Down DP
# O(mnk) time | O(mnk) space
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(length, maxV, left_k):
            if left_k == 0 or left_k > maxV:
                return 0
            if length == 1:
                return 1 if left_k == 1 else 0
            
            ans = maxV * dp(length - 1, maxV, left_k)
            for v in range(1, maxV):
                ans += dp(length - 1, v, left_k - 1)
                ans %= MOD

            return ans

        ans = 0
        for num in range(1, m + 1):
            ans += dp(n, num, k)
        
        return ans % MOD

# 2nd solution, Bottom-Up DP
# O(mnk) time | O(mnk) space
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0 or k > m:
            return 0
        MOD = 10**9 + 7
        dp = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
        # the array has length of 1, and 1 jump, only 1 way to do that, for any k
        for maxV in range(1, m + 1):
            dp[1][1][maxV] = 1
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for maxV in range(m + 1):
                    dp[i][j][maxV] += dp[i - 1][j][maxV] * maxV
                    dp[i][j][maxV] += sum(dp[i - 1][j - 1][1:maxV])
        
        return sum(dp[n][k][1:]) % MOD