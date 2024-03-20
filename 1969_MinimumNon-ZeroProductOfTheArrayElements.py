# 1st solution
# O(p) time | O(1) space
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1_000_000_007
        k = (1 << p) - 1
        return k * pow(k - 1, k >> 1, MOD) % MOD