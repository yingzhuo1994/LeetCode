# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        MOD = 10**9 + 7

        @cache
        def dfs(i, j):
            value = grid[i][j]
            count = 1
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] > value:
                    count += dfs(x, y)
            return count % MOD       

        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
                ans %= MOD
        
        return ans