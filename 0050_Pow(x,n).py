# 1st recursive solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        result = self.myPow(x, n // 2) * self.myPow(x, n // 2)
        if n & 1 == 1:
            result *= x
        return result

# 2nd iterative solution
# O(log(n)) time | O(1) space
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n = n // 2
        return result
