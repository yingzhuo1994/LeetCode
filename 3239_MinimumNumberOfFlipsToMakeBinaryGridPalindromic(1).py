# 1st solution
# O(mn) time | O(1) space
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count1 = 0
        for row in grid:
            i, j = 0, n - 1
            while i < j:
                if row[i] != row[j]:
                    count1 += 1
                i += 1
                j -= 1
        count2 = 0
        for col in range(n):
            i, j = 0, m - 1
            while i < j:
                if grid[i][col] != grid[j][col]:
                    count2 += 1
                i += 1
                j -= 1
        return min(count1, count2)