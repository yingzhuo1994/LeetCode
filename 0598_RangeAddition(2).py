# 1st solution
# O(len(ops)) time | O(1) space
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m - 1, n - 1
        for a, b in ops:
            x = min(x, a - 1)
            y = min(y, b - 1)
        return (x + 1) * (y + 1)