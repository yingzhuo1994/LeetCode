# 1st solution, recursion
# O(n) time | O(n) space
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n == 1:
            return chr(ord("a") + k - 1)
        if k - n > 25:
            return self.getSmallestString(n - 1, k - 26) + "z"
        else:
            return "a" * (n - 1) + chr(ord("a") + k - n)