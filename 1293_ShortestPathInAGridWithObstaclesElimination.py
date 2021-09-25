class Solution:
    # 1st solution, TLE
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ans = [float("inf")]
        self.dfs(grid, 0, 0, 0, k, ans)
        return ans[0] if ans[0] != float("inf") else -1
    
    def dfs(self, grid, i, j, steps, k, ans):
        if k < 0:
            return 
        m = len(grid)
        n = len(grid[0])
        if ans[0] == m + n - 2:
            return 
        if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] == "#":
            return 
        if (i, j) == (m - 1, n - 1):
            ans[0] = min(ans[0], steps)
            return 
        
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            tmp = grid[i][j]
            grid[i][j] = "#"
            if tmp == 1:
                self.dfs(grid, i + x, j + y, steps + 1, k - 1, ans)
            else:
                self.dfs(grid, i + x, j + y, steps + 1, k, ans)
            grid[i][j] = tmp


    # 2nd solution
    # O(m * n * (m + n))
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        Q, v = deque([(0, 0, 0, k)]), set()
        
        if k >= m + n - 2: 
            return m + n - 2
        
        while Q:
            steps, x, y, k = Q.popleft()
            if (x, y) == (n-1, m-1): return steps
            
            for dx, dy in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= dx < n and 0 <= dy < m and k - grid[dy][dx] >= 0:
                    new = (dx, dy, k - grid[dy][dx])
                    if new not in v:
                        v.add(new)
                        Q.append((steps + 1,) + new)
            
        return -1