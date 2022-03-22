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

# 2nd solution, iteration
# O(n) time | O(n) space
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if (k - n) % 25 == 0:
            zCount = (k - n) // 25
            aCount = n - zCount
            xCh = ""
        else:
            zCount = (k - n) // 25
            x = (k - n) % 25 + 1
            xCh = chr(ord("a") + x - 1)
            aCount = n - zCount - 1
        return "a" * aCount + xCh + "z" * zCount 