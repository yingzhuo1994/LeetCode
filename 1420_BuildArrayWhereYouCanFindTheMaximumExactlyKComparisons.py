# 1st solution
# O(mn) time | O(mn) space
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