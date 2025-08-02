# 1st solution
# O(1) time | O(1) space
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD =10**9 + 7
        q = n >> 1
        r = n & 1
        if r == 1:
            num = pow(20, q, MOD) * 5
        else:
            num = pow(20, q, MOD)
        ans = num % MOD
        return ans