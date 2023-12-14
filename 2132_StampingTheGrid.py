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
    
# 2nd solution
# O(mn) time | O(mn) space
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        # 1. 计算 grid 的二维前缀和
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        # 2. 计算二维差分
        # 为方便第 3 步的计算，在 d 数组的最上面和最左边各加了一行（列），所以下标要 +1
        d = [[0] * (n + 2) for _ in range(m + 2)]
        for i2 in range(stampHeight, m + 1):
            for j2 in range(stampWidth, n + 1):
                i1 = i2 - stampHeight + 1
                j1 = j2 - stampWidth + 1
                if s[i2][j2] - s[i2][j1 - 1] - s[i1 - 1][j2] + s[i1 - 1][j1 - 1] == 0:
                    d[i1][j1] += 1
                    d[i1][j2 + 1] -= 1
                    d[i2 + 1][j1] -= 1
                    d[i2 + 1][j2 + 1] += 1

        # 3. 还原二维差分矩阵对应的计数矩阵（原地计算）
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                d[i + 1][j + 1] += d[i + 1][j] + d[i][j + 1] - d[i][j]
                if v == 0 and d[i + 1][j + 1] == 0:
                    return False
        return True