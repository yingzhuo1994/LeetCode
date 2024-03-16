# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n - 1):
            for i in range(m):
                if j > 0 and dp[i][j] == 0:
                    continue
                if i > 0 and grid[i-1][j+1] > grid[i][j]:
                    dp[i-1][j+1] = max(dp[i-1][j+1], dp[i][j] + 1)
                if grid[i][j+1] > grid[i][j]:
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j] + 1)
                if i + 1 < m and grid[i+1][j+1] > grid[i][j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
        return max(map(max, dp))


# 2nd solution
# O(mn) time | O(m) space
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        level = set([i for i in range(m)])
        step = 0
        while step < n - 1:
            newLevel = set()
            for i in level:
                for j in [i-1, i, i+1]:
                    if 0 <= j < m and grid[j][step+1] > grid[i][step]:
                        newLevel.add(j)
            if not newLevel:
                break
            level = newLevel
            step += 1
        return step

# 3rd solution
# O(mn) time | O(1) space
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid:
            row[0] *= -1  # 入队标记
        for j in range(n - 1):
            for i, row in enumerate(grid):
                if row[j] > 0:  # 不在队列中
                    continue
                for k in [i - 1, i, i + 1]:
                    if 0 <= k < m and grid[k][j + 1] > -row[j]:
                        grid[k][j + 1] *= -1  # 入队标记
            if all(row[j + 1] > 0 for row in grid):  # 无法再往右走了
                return j
        return n - 1