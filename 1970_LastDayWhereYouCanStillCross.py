# 1st solution
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(col*row + 2)

        grid = [[1] * col for _ in range(row)]
        neibs = [[0,1],[0,-1],[1,0],[-1,0]]
        cells = [(x-1, y-1) for x, y in cells]

        def index(x, y):
            return x * col + y + 1

        for i in reversed(range(len(cells))):
            x, y = cells[i][0], cells[i][1]

            grid[x][y] = 0
            for dx, dy in neibs:
                a = x + dx
                b = y + dy
                ind = index(a, b)
                if 0 <= a < row and 0 <= b < col and grid[a][b] == 0:
                    dsu.union(ind, index(x, y))
            if x == 0:
                dsu.union(0, index(x, y))
            if x == row - 1:
                dsu.union(col*row + 1, index(x, y))

            if dsu.find(0) == dsu.find(col*row + 1):
                return i

class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

# 2nd solution, Binary Search + BFS
# O(mn * log(k)) time | O(mn) space
# k = len(cells)
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]

        def canWalkFromTopToBottom(dayAt):
            grid = [[0] * col for _ in range(row)]  # Create grid in the `dayAt` th date
            for i in range(dayAt):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1  # Mark as water

            bfs = deque([])
            for c in range(col):
                if grid[0][c] == 0:  # Add all valid start cells in the top row
                    bfs.append((0, c))
                    grid[0][c] = 1  # Mark as visited

            while bfs:
                r, c = bfs.popleft()
                if r == row - 1: 
                    return True  # Reach to bottom -> Return Valid
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == row or nc < 0 or nc == col or grid[nr][nc] == 1: 
                        continue
                    grid[nr][nc] = 1  # Mark as visited
                    bfs.append((nr, nc))
            return False

        left, right = 1, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if canWalkFromTopToBottom(mid):
                ans = mid  # Update current answer so far
                left = mid + 1  # Try to find a larger day
            else:
                right = mid - 1  # Try to find a smaller day
        return ans