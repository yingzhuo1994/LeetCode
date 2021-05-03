class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1st recursive solution
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        result = self.myPow(x, n // 2) * self.myPow(x, n // 2)
        if n % 2 == 1:
            result *= x
        return result

        # 2nd iterative solution
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n % 2 == 1:
                pow *= x
            x *= x
            n = n // 2
        return pow
