# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            cnt = 0
            level = deque([(i, j)])
            while level:
                x, y = level.popleft()
                if grid[x][y] > 0:
                    cnt += grid[x][y]
                    grid[x][y] = 0
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        a = x + dx
                        b = y + dy
                        if 0 <= a < m and 0 <= b < n and grid[a][b] > 0:
                            level.append((a, b))
            return cnt
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    cnt = bfs(i, j)
                    ans = max(ans, cnt)
        return ans