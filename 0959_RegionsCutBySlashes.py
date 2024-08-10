# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        if n == 1:
            if grid[0][0] != " ":
                return 2
            else:
                return 1
        total = 4 * n + 1
        graph = [[0 for _ in range(total)] for _ in range(total)]
        
        for i in range(n):
            row = grid[i].replace("\\", "+")
            for j in range(n):
                if row[j] == "/":
                    for d in range(5):
                        graph[4 * i + d][4 * j + 4 - d] = 1
                elif row[j] == "+":
                    for d in range(5):
                        graph[4 * i + d][4 * j + d] = 1
        def dfs(x, y):
            graph[x][y] = 1
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                i = x + dx
                j = y + dy
                if 0 <= i < total and 0 <= j < total and graph[i][j] == 0:
                    dfs(i, j)

        ans = 0
        for i in range(total):
            for j in range(total):
                if graph[i][j] == 1:
                    continue
                ans += 1
                dfs(i, j)
        return ans

