class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        q = x
        num = 0
        while x > 0:
            num += x % 10
            x //= 10
        if q % num == 0:
            return num
        return -1