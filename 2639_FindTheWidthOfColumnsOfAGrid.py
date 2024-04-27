# 1st solution
# O(mn) time | O(n) space
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * n
        for i in range(m):
            for j in range(n):
                ans[j] = max(ans[j], len(str(grid[i][j])))
        return ans