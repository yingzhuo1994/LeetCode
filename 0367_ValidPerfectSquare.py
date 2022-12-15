# 1st solution
# O(n) time | O(1) space
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k = 2
        while k * k <= num:
            if k * k == num:
                return True
            if num % (k * k) == 0:
                num //=  k * k
                k = 1
            k += 1
        return num == 1

# 2nd solution
# O(log(n)) time | O(1) space
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + num // r) // 2
        return r * r == num