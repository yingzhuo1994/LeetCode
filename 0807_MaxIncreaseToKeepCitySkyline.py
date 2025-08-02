# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = [0 for _ in range(n)]
        colMax = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[j] = max(colMax[j], grid[i][j])
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(rowMax[i], colMax[j]) - grid[i][j]
        return ans