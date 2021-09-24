class Solution:
    # O(n) time | O(1) space
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        t0 = 0
        t1 = 1
        t2 = 1
        while n > 2:
            t0, t1, t2 = t1, t2, t0 + t1 + t2
            n -= 1
        return t2