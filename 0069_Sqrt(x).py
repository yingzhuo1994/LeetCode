class Solution:
    def mySqrt(self, x: int) -> int:
        # 1st solution
        # def f(k):
        #     return k * k - x
        # a, b = 0, x
        # while a <= b:
        #     c = (a + b) // 2
        #     if f(c) <= 0 and f(c + 1) > 0:
        #         return c
        #     if f(c) < 0:
        #         a = c + 1
        #     else:
        #         b = c - 1

        # 2nd Newton Iteration method
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return r
