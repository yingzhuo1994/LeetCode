class Solution:
    # O(R * C) time | O(R * C) space
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curArea = self.dfs(grid, i, j, 0)
                maxArea = max(maxArea, curArea)
        return maxArea
    
    def dfs(self, grid, i, j, curLength):
        if grid[i][j] != 1:
            return 0
        curLength += 1
        grid[i][j] = "#"
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            row, col = i + x, j + y
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                curLength += self.dfs(grid, row, col, 0)
        return curLength