# 1st solution
# O(n) time | O(1) space
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        rev = -1
        while n > 1:
            m = 1 << (n - 1)
            if k > m:
                k = 2 * m - k
                rev *= -1
            elif k == m:
                return "0" if rev > 0 else "1"
            n -= 1

        if rev > 0:
            return "1"
        else:
            return "0"