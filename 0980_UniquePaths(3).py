# 1st solution
# O(3^mn) time | O(mn) space
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        end = (0, 0)
        emptyCellCount = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    emptyCellCount += 1

        self.result = 0
        def dfs(i, j, pathLength):
            if (i, j) == end and pathLength == emptyCellCount+1:
                self.result += 1
                return 
            if 0 <= i < m and 0 <= j < n and grid[i][j] in (0, 1):
                tmp = grid[i][j]
                grid[i][j] = "#"
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = i + x, j + y
                    dfs(row, col, pathLength + 1)
                grid[i][j] = tmp
        
        dfs(start[0], start[1], 0)
        return self.result