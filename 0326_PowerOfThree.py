# 1st solution
# O(1) time | O(1) space
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0

# 2nd loop iteration solution
# O(logn) time | O(1) space
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1
