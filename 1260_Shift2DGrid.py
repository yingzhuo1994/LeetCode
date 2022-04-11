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