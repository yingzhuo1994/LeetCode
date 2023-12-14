# 1st solution, TLE
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        def dfs(i, j):
            for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                row = i + dx * (stampHeight - 1)
                col = j + dy * (stampWidth - 1)
                if 0 <= row < m and 0 <= col < n:
                    rowStart = min(i, row)
                    rowEnd = max(i, row)
                    colStart = min(j, col)
                    colEnd = max(j, col)
                    valid = True
                    for x in range(rowStart, rowEnd + 1):
                        for y in range(colStart, colEnd + 1):
                            if grid[x][y] == 1:
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        for x in range(rowStart, rowEnd + 1):
                            for y in range(colStart, colEnd + 1):
                                grid[x][y] = -1

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return False
        return True