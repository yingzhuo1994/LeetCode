# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h > 0:
                    ans += 2
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        ans += max(0, grid[x][y] - h)
                    else:
                        ans += h
        return ans