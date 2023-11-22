# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dic = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dic[grid[i][j]] = (i, j)
        graph = [[[] for _ in range(n)] for _ in range(m)]
        for i in range(len(moveCost)):
            for j in range(len(moveCost[i])):
                x, y = dic[i]
                graph[x][y].append([j, moveCost[i][j]])
        # for line in graph:
        #     print(line)
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        # print(dp)
        for i in range(m - 1):
            for j in range(n):
                for y, cost in graph[i][j]:
                    dp[i + 1][y] = min(dp[i + 1][y], dp[i][j] + cost + grid[i+1][y])
        return min(dp[-1])