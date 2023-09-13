# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        steps = 0
        n = len(grid)
        a, b = -1, -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    a, b = i, j
                    break
            if a != -1:
                break
        if (a, b) != (0, 0):
            return False
        i, j = 0, 0

        while steps < n * n - 1:
            valid = False
            for dx, dy in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n and grid[x][y] == steps + 1:
                    i, j = x, y
                    steps += 1
                    valid = True
                    break

            if not valid:
                return False
        return True
