# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        def dfs(i, j):
            if grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            ans = grid1[i][j] == 1
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1:
                    if not dfs(x, y):
                        ans = False
            return ans
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    count += dfs(i, j)
        return count
