# 1st solution
# O(mn * log(mn)) time | O(mn) space
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        nums = [[mat[i][j], i, j] for i in range(m) for j in range(n)]
        nums.sort()
        dp = [[1 for _ in range(n)] for _ in range(m)]
        maxRows = [[] for _ in range(m)]
        maxCols = [[] for _ in range(n)]
        for num, i, j in nums:
            if maxRows[i]:
                k = maxRows[i][-1]
                if num > mat[i][k]:
                    dp[i][j] = dp[i][k] + 1
                    maxRows[i].append(j)
                elif len(maxRows[i]) > 1:
                    dp[i][j] = dp[i][maxRows[i][-2]] + 1
            else:
                maxRows[i].append(j)
            
            if maxCols[j]:
                k = maxCols[j][-1]
                if num > mat[k][j]:
                    dp[i][j] = max(dp[i][j], dp[k][j] + 1)
                    maxCols[j].append(i)
                elif len(maxCols[j]) > 1:
                    dp[i][j] = max(dp[i][j], dp[maxCols[j][-2]][j] + 1)
            else:
                maxCols[j].append(i)
            
            if dp[i][j] > dp[i][maxRows[i][-1]]:
                maxRows[i][-1] = j
            if dp[i][j] > dp[maxCols[j][-1]][j]:
                maxCols[j][-1] = i

        return max([max(line) for line in dp])
    

# 2nd solution
# O(mn * log(mn)) time | O(mn) space
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i, j))  # 相同元素放在同一组，统计位置

        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in sorted(g.items(), key=lambda p: p[0]):
            # 先把最大值算出来，再更新 row_max 和 col_max
            mx = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            for (i, j), f in zip(pos, mx):
                row_max[i] = max(row_max[i], f)  # 更新第 i 行的最大 f 值
                col_max[j] = max(col_max[j], f)  # 更新第 j 列的最大 f 值
        return max(row_max)