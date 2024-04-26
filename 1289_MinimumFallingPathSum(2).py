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

# 3rd solution
# O(n^2) time | O(1) space
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for pre_row, cur_row in pairwise(grid):  # 枚举上一行和当前行
            mn, mn2 = nsmallest(2, pre_row)  # 上一行的最小值和次小值
            for j, pre in enumerate(pre_row):  # 枚举上一行的状态
                cur_row[j] += mn if pre != mn else mn2  # 不是最小就加上最小，否则加上次小
        return min(grid[-1])  # 第 n-1 行的最小值


# 4th solution
# O(n^2) time | O(1) space
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def getTwoSmallest(row):
            mn, mn2 = float("inf"), float("inf")
            idx, idx2 = -1, -1
            for i, val in enumerate(row):
                if val < mn:
                    mn, mn2 = val, mn
                    idx, idx2 = i, idx
                elif val < mn2:
                    mn2 = val
                    idx2 = i
            return mn, mn2, idx, idx2
        
        n = len(grid)
        pre_row = grid[0]
        m1, m2, idx, idx2 = getTwoSmallest(pre_row)
        for i in range(1, n):
            mn1, mn2 = float("inf"), float("inf")
            col1, col2 = -1, -1
            for j, val in enumerate(grid[i]):
                if j != idx:
                    if val + m1 < mn1:
                        mn1, mn2 = val + m1, mn1
                        col1, col2 = j, col1
                    elif val + m1 < mn2:
                        mn2 = val + m1
                        col2 = j
                elif j != idx2:
                    if val + m2 < mn1:
                        mn1, mn2 = val + m2, mn1
                        col1, col2 = j, col1
                    elif val + m2 < mn2:
                        mn2 = val + m2
                        col2 = j
            m1, m2, idx, idx2 = mn1, mn2, col1, col2
        return min(m1, m2)  # 第 n-1 行的最小值