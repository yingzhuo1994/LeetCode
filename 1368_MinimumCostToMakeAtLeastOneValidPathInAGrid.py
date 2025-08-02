# 1st solution
# O(mn * log(mn)) time | O(mn) space
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[m * n for _ in range(n)] for _ in range(m)]
        neighbers = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        dp[0][0] = 0
        minHeap = [[0, 0, 0]]
        while minHeap:
            cost, i, j = heappop(minHeap)
            if (i, j) == (m - 1, n - 1):
                return cost
            if cost > dp[i][j]:
                continue
            for idx in range(1, 5):
                dx, dy = neighbers[idx]
                x = i + dx
                y = j + dy
                newCost = cost + (not idx == grid[i][j])
                if 0 <= x < m and 0 <= y < n and dp[x][y] > newCost:
                    dp[x][y] = newCost
                    heappush(minHeap, [newCost, x, y])