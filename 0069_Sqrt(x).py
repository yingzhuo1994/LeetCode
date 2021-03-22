class Solution:
    def mySqrt(self, x: int) -> int:
        def f(k):
            return k * k - x
        a, b = 0, x
        c = (a + b) / 2
        while a <= b:
            # print(a, b, c)
            # print(f(a), f(b), f(c))
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c
            if f(int(c)) <= 0 and f(int(c) + 1) > 0:
                return int(c)
            c = (a + b) / 2
