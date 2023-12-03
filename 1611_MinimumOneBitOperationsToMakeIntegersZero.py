# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)

# 2nd solution
# O(log(n)) time | O(log(n)) space
class Solution:
    @cache
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 3
        d = len(bin(n)) - 2
        return 2**d - 1 -  self.minimumOneBitOperations(n - 2**d)