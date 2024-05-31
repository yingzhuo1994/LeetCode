# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a, b = None, None
        for i in range(n):
            for j in range(n):
                num = abs(grid[i][j])
                x, y = divmod(num - 1, n)
                if grid[x][y] < 0:
                    a = num
                else:
                    grid[x][y] = -abs(grid[x][y])
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    b = i * n + j + 1
                    break

        return [a, b]
