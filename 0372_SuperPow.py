# 1st solution
# O(n) time | O(n) space
# where n is the length of b
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 0:
            return 0
        MOD = 1337
        if a >= MOD:
            return self.superPow(a % MOD, b)
        if len(b) > 1:
            r = b.pop()
            x1 = self.superPow(a**10, b)
            x2 = a**r % MOD
            return x1 * x2 % MOD
        return a**b[0] % MOD
