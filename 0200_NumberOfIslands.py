class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lst = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                length = self.lookIslands(grid, i, j)
                if length > 0:
                    lst.append(length)
        return len(lst)
    
    def lookIslands(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = 'X'
            length = 1 + self.lookIslands(grid, i + 1, j) + self.lookIslands(grid, i - 1, j)\
                       + self.lookIslands(grid, i, j + 1) + self.lookIslands(grid, i, j - 1)
            return length
        else:
            return 0