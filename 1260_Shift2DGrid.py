# 1st solution
# O(mn) time | O(mn) space
# where m, n are the size of grid
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0]) 
        newGrid = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                x, y = self.getNextPlace(row, col, i, j, k)
                newGrid[x][y] = grid[i][j]
        return newGrid
    
    def getNextPlace(self, row, col, i, j, k):
        idx = i * col + j + k
        x = (idx // col) % row
        y = idx % col
        return x, y

# 2nd solution
# O(mn) time | O(1) space
# where m, n are the size of grid
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        k %= row * col
        if k == 0:
            return grid
        self.rotate(grid, 0, 0, row - 1, col - 1)
        for line in grid:
            print(line)
        frontEndRow, frontEndCol = self.getNextPlace(row, col, 0, 0, k - 1)
        backStartRow, backStartCol = self.getNextPlace(row, col, 0, 0, k)
        self.rotate(grid, 0, 0, frontEndRow, frontEndCol)
        self.rotate(grid, backStartRow, backStartCol, row - 1, col - 1)
        return grid
    
    def rotate(self, grid, startRow, startCol, endRow, endCol):
        row, col = len(grid), len(grid[0])
        startIdx = self.getIdx(col, startRow, startCol)
        endIdx = self.getIdx(col, endRow, endCol)
        while startIdx < endIdx:
            self.swap(grid, startRow, startCol, endRow, endCol)
            startRow, startCol = self.getNextPlace(row, col, startRow, startCol, 1)
            endRow, endCol = self.getNextPlace(row, col, endRow, endCol, -1)
            startIdx = self.getIdx(col, startRow, startCol)
            endIdx = self.getIdx(col, endRow, endCol)

    def getIdx(self, col, i, j):
        return i * col + j

    def getNextPlace(self, row, col, i, j, k):
        idx = i * col + j + k
        x = (idx // col) % row
        y = idx % col
        return x, y
    
    def swap(self, grid, x1, y1, x2, y2):
        grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]