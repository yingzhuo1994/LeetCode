# 1st solution
# O(n) time | O(1) space
class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        startMoney = 0
        for i in range(n):
            if i % 7 == 0:
                startMoney += 1
            money += startMoney + i % 7
        return money

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def totalMoney(self, n: int) -> int:
        a, b = divmod(n, 7)
        a1 = (1 + 7) * 7 // 2
        an = (a + (a + 6)) * 7 // 2
        s1 = (a1 + an) * a // 2
        a += 1
        s2 = (a + (a + b - 1)) * b // 2
        return s1 + s2

