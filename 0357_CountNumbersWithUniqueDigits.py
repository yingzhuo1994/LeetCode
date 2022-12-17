# 1st solution
# O(1) time | O(1) space
from math import factorial
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            count = 10
            for d in range(2, n + 1):
                count += 9 * (factorial(8) // factorial(9-d) + (d - 1) * factorial(8) // factorial(10 - d))
            return count