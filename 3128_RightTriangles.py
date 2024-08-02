# 1st solution
# O(mn + n^2) time | O(mn) space
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [[] for _ in range(m)]
        cols = [[] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i].append(j)
                    cols[j].append(i)
        ans = 0
        for k in range(n):
            if len(cols[k]) <= 1:
                continue
            lst_1 = rows[cols[k][0]]
            count = max(len(lst_1) - 1, 0)
            for i in range(1, len(cols[k])):
                ans += count
                lst_1 = rows[cols[k][i]]
                count += max(len(lst_1) - 1, 0)
            
            lst_2 = rows[cols[k][-1]]
            count = max(len(lst_2) - 1, 0)
            for i in reversed(range(len(cols[k]) - 1)):
                ans += count
                lst_2 = rows[cols[k][i]]
                count += max(len(lst_2) - 1, 0)

        return ans