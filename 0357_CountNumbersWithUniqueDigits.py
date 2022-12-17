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

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        
        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product
            
        return ans