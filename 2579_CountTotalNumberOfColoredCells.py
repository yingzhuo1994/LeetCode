# 1st solution
# O(n) time | O(1) space
class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 1
        for i in range(2, n + 1):
            ans += (i - 1) * 4
        return ans
