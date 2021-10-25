class Solution:
    # 1st solution, TLE
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ans = [float("inf")]
        self.bfs(grid, 0, 0, 0, k, ans)
        return ans[0] if ans[0] != float("inf") else -1
    
    def bfs(self, grid, i, j, steps, k, ans):
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
            self.bfs(grid, i + x, j + y, steps + 1, k - tmp, ans)
            grid[i][j] = tmp


    # 2nd solution
    # O(m * n * k) time | O(m * n * k) space
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        stack, visited = deque([(0, 0, 0, k)]), set()
        
        if k >= m + n - 2: 
            return m + n - 2
        
        while stack:
            steps, i, j, k = stack.popleft()
            if (i, j) == (m-1, n-1): return steps
            
            for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                row, col = i + x, j + y
                if 0 <= row < m and 0 <= col < n and k - grid[row][col] >= 0:
                    new = (row, col, k - grid[row][col])
                    if new not in visited:
                        visited.add(new)
                        stack.append((steps + 1,) + new)
            
        return -1