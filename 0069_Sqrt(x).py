class Solution:
    def mySqrt(self, x: int) -> int:
        def f(k):
            return k * k - x
        a, b = 0, x
        while a <= b:
            c = (a + b) // 2
            if f(c) <= 0 and f(c + 1) > 0:
                return c
            if f(c) < 0:
                a = c + 1
            else:
                b = c - 1
