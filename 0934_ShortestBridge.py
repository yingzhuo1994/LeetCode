# 1st solution
# O(n^4) time | O(n^2) space
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j, lst):
            if grid[i][j] == 1:
                lst.append([i, j])
                grid[i][j] = -1
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        dfs(x, y, lst)
        
        lst1 = []
        lst2 = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if len(lst1) == 0:
                        dfs(i, j, lst1)
                    else:
                        dfs(i, j, lst2)
        
        ans = float("inf")
        for x0, y0 in lst1:
            for x1, y1 in lst2:
                dist = abs(x1 - x0) + abs(y1 - y0) - 1
                ans = min(ans, dist)
        
        return ans
                