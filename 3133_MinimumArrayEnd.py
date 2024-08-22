# 1st solution
# O(1) time | O(1) space
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        mask = n - 1
        i = 0
        d = 0
        while (1 << d) <= mask:
            while x & (1 << i):
                i += 1
            if mask & (1 << d):
                x |= (1 << i)
            d += 1
            i += 1
        return x