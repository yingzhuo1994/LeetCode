class Solution:
    # 1st solution
    # O(n) time | O(1) space
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4 - self.counterConnection(grid, i, j)
        return perimeter
    
    def counterConnection(self, grid, i, j):
        count = 0
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            row = i + x
            col = j + y
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                count += grid[row][col]
        return count