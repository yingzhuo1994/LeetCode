# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[-1 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                ans[i-1][j-1] = max([grid[i + dx][j + dy] for dx in [-1, 0, 1] for dy in [-1, 0, 1]])
        return ans