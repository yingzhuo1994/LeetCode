# 1st solution
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.loc = {grid[i][j]: (i, j) for i in range(len(grid)) for j in range(len(grid[i]))}
        self.size = len(grid)

    def adjacentSum(self, value: int) -> int:
        i, j = self.loc[value]
        ans = 0
        if i - 1 >= 0:
            ans += self.grid[i - 1][j]
        if i + 1 < self.size:
            ans += self.grid[i + 1][j]
        if j - 1 >= 0:
            ans += self.grid[i][j - 1]
        if j + 1 < self.size:
            ans += self.grid[i][j + 1]
        return ans

    def diagonalSum(self, value: int) -> int:
        i, j = self.loc[value]
        ans = 0
        if i - 1 >= 0 and j - 1 >= 0:
            ans += self.grid[i - 1][j - 1]
        if i + 1 < self.size and j + 1 < self.size:
            ans += self.grid[i + 1][j + 1]
        if i - 1 >= 0 and j + 1 < self.size:
            ans += self.grid[i - 1][j + 1]
        if i + 1 < self.size and j - 1 >= 0:
            ans += self.grid[i + 1][j - 1]
        return ans        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)