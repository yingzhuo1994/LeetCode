def c2(n: int) -> int:
    return n * (n - 1) // 2 if n > 1 else 0

# 1st solution
# O(1) time | O(1) space
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return c2(n + 2) - 3 * c2(n - limit + 1) + 3 * c2(n - 2 * limit) - c2(n - 3 * limit - 1)
