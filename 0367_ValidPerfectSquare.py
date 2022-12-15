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