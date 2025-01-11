# 1st solution
# O(n) time | O(1) space
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans = 0
        for i in range(4):
            r1 = num1 % 10
            r2 = num2 % 10
            r3 = num3 % 10
            d = min(r1, r2, r3)
            num1 //= 10
            num2 //= 10
            num3 //= 10
            ans += d * pow(10, i)
        return ans