# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in walls:
            grid[i][j] = -1
        for i, j in guards:
            grid[i][j] = 2
        dic = {(i, j): [False, False, False, False] for i, j in guards}
        for i, j in guards:
            for k in range(4):
                if dic[(i, j)][k]:
                    continue
                dic[(i, j)][k] = True
                x, y = i, j
                # top
                if k == 0:
                    dx = -1
                    while x + dx >= 0:
                        if grid[x + dx][y] in [0, 1]:
                            grid[x + dx][y] = 1
                            x += dx
                        elif grid[x + dx][y] == 2:
                            dic[(x + dx, y)][2] = False
                            break
                        else:
                            break
                # right
                elif k == 1:
                    dy = 1
                    while y + dy < n:
                        if grid[x][y + dy] in [0, 1]:
                            grid[x][y + dy] = 1
                            y += dy
                        elif grid[x][y + dy] == 2:
                            dic[(x, y + dy)][3] = False
                            break
                        else:
                            break
                # bottom
                elif k == 2:
                    dx = 1
                    while x + dx < m:
                        if grid[x + dx][y] in [0, 1]:
                            grid[x + dx][y] = 1
                            x += dx
                        elif grid[x + dx][y] == 2:
                            dic[(x + dx, y)][0] = False
                            break
                        else:
                            break
                # left
                else:
                    dy = -1
                    while y + dy >= 0:
                        if grid[x][y + dy] in [0, 1]:
                            grid[x][y + dy] = 1
                            y += dy
                        elif grid[x][y + dy] == 2:
                            dic[(x, y + dy)][1] = False
                            break
                        else:
                            break
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count
                