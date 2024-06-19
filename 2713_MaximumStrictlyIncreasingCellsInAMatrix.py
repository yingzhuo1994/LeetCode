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
    
