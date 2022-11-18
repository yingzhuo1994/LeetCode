# 1st solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n in {1, 2, 3, 5}:
            return True
        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)
        return False

# 2nd solution
# O(log(n)) time | O(1) space
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while True:
            if n in {1, 2, 3, 5}:
                return True
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False