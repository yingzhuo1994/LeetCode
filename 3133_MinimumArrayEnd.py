# 1st solution
# O(log(n) + log(x)) time | O(1) space
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


# 2nd solution
# O(log(n)) time | O(1) space
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        j = 0
        t = ~x
        while n >> j:
            lb = t & -t
            x |= (n >> j & 1) * lb
            j += 1
            t ^= lb
        return x
