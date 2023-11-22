# 1st solution
# O(mn^2) time | O(mn) space
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(m - 1):
            for j in range(n):
                for y, cost in enumerate(moveCost[grid[i][j]]):
                    dp[i + 1][y] = min(dp[i + 1][y], dp[i][j] + cost + grid[i+1][y])
        return min(dp[-1])

# 2nd solution
# O(mn^2) time | O(1) space
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m - 2, -1, -1):
            for j in range(n):
                grid[i][j] += min(g + c for g, c in zip(grid[i + 1], moveCost[grid[i][j]]))
        return min(grid[0])