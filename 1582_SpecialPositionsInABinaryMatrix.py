# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = {i: [] for i in range(m)}
        columns = {j: [] for j in range(n)}
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rows[i].append(j)
                    columns[j].append(i)
        ans = 0
        for i in range(m):
            if len(rows[i]) == 1:
                j = rows[i][0]
                if len(columns[j]) == 1:
                    ans += 1
        return ans