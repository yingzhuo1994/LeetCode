# 1st solution
# O(n^3) time | O(n^2) space
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp =[[float("inf") for _ in range(n)] for _ in range(n)]
        dp[0] = grid[0]
        for i in range(n - 1):
            for j in range(n):
                for k in range(n):
                    if j == k:
                        continue
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j] + grid[i+1][k])
        return min(dp[-1])


# 2nd solution
# O(n^2 * log(n)) time | O(n) space
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        level = {-1: 0}
        for row in grid:
            pairs = [[val, i] for i, val in enumerate(row)]
            pairs.sort()
            newLevel = {}
            for i, a in level.items():
                for b, j in pairs[:3]:
                    if i == j:
                        continue
                    newLevel[j] = min(newLevel.get(j, float("inf")), a + b)
            items = sorted(list([val, col] for col, val in newLevel.items()))
            level = {items[0][1]: items[0][0], items[1][1]: items[1][0]}

        return min(level.values())