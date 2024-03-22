# 1st solution, TLE
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        level = [[0, 0]]
        while level:
            newLevel = []
            for i, j in level:
                for k in range (j + 1, min(grid[i][j] + j + 1, n)):
                    if dp[i][k] > 0:
                        continue
                    dp[i][k] = dp[i][j] + 1
                    newLevel.append([i, k])
                for k in range(i + 1, min(grid[i][j] + i + 1, m)):
                    if dp[k][j] > 0:
                        continue
                    dp[k][j] = dp[i][j] + 1
                    newLevel.append([k, j])
            level = newLevel

        return dp[-1][-1]

# 2nd solution
# O(mn(log(m) + log(n))) time | O(mn) space
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        col_heaps = [[] for _ in grid[0]]  # 每一列的最小堆
        for i, row in enumerate(grid):
            row_h = []  # 第 i 行的最小堆
            for j, (g, col_h) in enumerate(zip(row, col_heaps)):
                while row_h and row_h[0][1] < j:  # 无法到达第 j 列
                    heappop(row_h)  # 弹出无用数据
                while col_h and col_h[0][1] < i:  # 无法到达第 i 行
                    heappop(col_h)  # 弹出无用数据
                f = inf if i or j else 1  # 起点算 1 个格子
                if row_h: f = row_h[0][0] + 1  # 从左边跳过来
                if col_h: f = min(f, col_h[0][0] + 1)  # 从上边跳过来
                if g and f < inf:
                    heappush(row_h, (f, g + j))  # 经过的格子数，向右最远能到达的列号
                    heappush(col_h, (f, g + i))  # 经过的格子数，向下最远能到达的行号
        return f if f < inf else -1  # 此时的 f 是在 (m-1, n-1) 处算出来的