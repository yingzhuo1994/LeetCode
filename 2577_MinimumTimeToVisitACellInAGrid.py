# 1st solution
# O(mn * log(mn)) time | O(mn) space
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m, n = len(grid), len(grid[0])
        dp = [[grid[i][j] for j in range(n)] for i in range(m)]
        minHeap = [[0, 0, 0]]
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[0][0] = True
        while minHeap:
            t, i, j = heappop(minHeap)
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if t + 1 >= grid[x][y]:
                        dp[x][y] = t + 1
                    else:
                        diff = grid[x][y] - (t + 1)
                        if diff & 1:
                            diff += 1
                        dp[x][y] = diff + (t + 1)
                    visited[x][y] = True
                    heappush(minHeap, [dp[x][y], x, y])
        return dp[-1][-1]

