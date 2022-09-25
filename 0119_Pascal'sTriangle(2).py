# 1st solution, recursion
# O(n^2) time | O(n^2) space
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last = self.getRow(rowIndex - 1)
        left = last + [0]
        right = [0] + last
        return [a + b for a, b in zip(left, right)]

# 2nd solution, iteration
# O(n^2) time | O(n) space
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        level = [1]
        for _ in range(rowIndex):
            left = level + [0]
            right = [0] + level
            level = [a + b for a, b in zip(left, right)]
        return level