# 1st solution
# O(1) time | O(1) space
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        if n == 1:
            return 1
        MOD = 10**9 + 7
        if 2 * n - 1 < target:
            ans = (1 + n) * n // 2
            ans %= MOD
            return ans 
        mid = target // 2
        k = n - mid
        ans = (1 + mid) * mid // 2 + (2 * target + k - 1) * k // 2
        ans %= MOD
        return ans