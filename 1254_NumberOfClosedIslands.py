# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j):
            if grid[i][j] < 0 or grid[i][j] == 1:
                return
            grid[i][j] = -1
            for dx, dy in neighbors:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    dfs(x, y)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i - 1, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)
        return ans            