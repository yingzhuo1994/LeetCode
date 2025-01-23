# 1st solution
# O(mn) time | O(m + n) space
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans += rows[i] > 1 or cols[j] > 1
        return ans