# 1st solution
# O(n) time | O(n) space
class Solution:
    @cache
    def divisorGame(self, n: int) -> bool:
        for i in range(1, n):
            if n % i == 0:
                val = n - i
                if not self.divisorGame(val):
                    return True
        return False