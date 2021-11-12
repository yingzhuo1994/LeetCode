# 1st solution
# O(mn) time | O(1) space
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if self.isAllRotten(grid):
            return 0
        
        rotten = self.getRotten(grid)
        steps = 0
        while rotten:
            steps += 1
            curRotten = []
            for i, j in rotten:
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = i + x, j + y
                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        grid[row][col] = 2
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

    def getRotten(self, grid):
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
        return rotten

# 2nd solution
# O(mn) time | O(1) space
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        for i,j in product(range(m), range(n)):
            if grid[i][j] == 2: queue.append((i,j))
            if grid[i][j] == 1: fresh += 1
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        levels = 0
        
        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))
                        
        return -1 if fresh != 0 else max(levels-1, 0)