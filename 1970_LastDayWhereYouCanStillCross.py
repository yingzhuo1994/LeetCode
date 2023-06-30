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
