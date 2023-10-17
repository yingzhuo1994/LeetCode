# 1st solution
# O(n) time | O(1) space
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                ans += num
        return ans

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def s(m: int) -> int:
            return n // m * (n // m + 1) // 2 * m
        return s(3) + s(5) + s(7) - s(15) - s(21) - s(35) + s(105)
