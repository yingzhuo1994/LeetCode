# 1st solution
# O(mn) time | O(1) space
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def flip(row):
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        for row in grid:
            if row[0] == 0:
                flip(row)
        m, n = len(grid), len(grid[0])
        ans = 0
        for j in range(n):
            count = 0
            for i in range(m):
                if grid[i][j] == 1:
                    count += 1
            d = max(count, m - count)
            ans += (1 << (n - 1 - j)) * d
        return ans