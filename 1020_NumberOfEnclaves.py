# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neig = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j):
            if grid[i][j] != 1:
                return None
            grid[i][j] = -1
            for dx, dy in neig:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    dfs(x, y)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1:
                    count += 1
        
        return count
            