class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        rotten = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                    visited.add((i, j))
        if self.isAllRotten(grid):
            return 0
        steps = 0
        while rotten:
            steps += 1
            curRotten = []
            for i, j in rotten:
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = i + x, j + y
                    if 0 <= row < m and 0 <= col < n and (row, col) not in visited and grid[row][col] == 1:
                        grid[row][col] = 2
                        visited.add((row, col))
                        curRotten.append((row, col))
            rotten = curRotten
        
        if self.isAllRotten(grid):
            return steps - 1
        else:
            return -1
    
    def isAllRotten(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return False
        return True
