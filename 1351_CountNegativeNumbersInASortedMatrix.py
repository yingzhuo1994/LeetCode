# 1st solution
# O(m + n) time | O(1) space
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        j = n - 1
        for row in grid:
            while j >= 0 and row[j] < 0:
                j -= 1
            count += n - 1 - j
        return count