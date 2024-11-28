# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[m * n for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0
        stack = deque([[0, 0]])
        def dfs(i, j):
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0 and dp[x][y] > dp[i][j]:
                        dp[x][y] = dp[i][j]
                        dfs(x, y)
                    if grid[x][y] == 1 and dp[x][y] > dp[i][j] + 1:
                        dp[x][y] = dp[i][j] + 1
                        stack.append([x, y])
        while stack:
            i, j = stack.popleft()
            dfs(i, j)
        return dp[-1][-1]

