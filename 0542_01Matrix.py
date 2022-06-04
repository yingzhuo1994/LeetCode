# 1st solution, dp
# O(r * c) time | O(1) space
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat and mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = float("inf")
                    if i > 0 and mat[i - 1][j] + 1 < mat[i][j]:
                        mat[i][j] = mat[i - 1][j] + 1
                    if j > 0 and mat[i][j - 1] + 1 < mat[i][j]:
                        mat[i][j] = mat[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    if i + 1 < m and mat[i + 1][j] + 1 < mat[i][j]:
                        mat[i][j] = mat[i + 1][j] + 1
                    if j + 1 < n and mat[i][j + 1] + 1 < mat[i][j]:
                        mat[i][j] = mat[i][j + 1] + 1
        return mat

# 2nd solution, back tracking
# O(r * c) time | O(r * c) space
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q, m, n = [], len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = 0x7fffffff
                else:
                    q.append((i, j))
        for i, j in q:
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = mat[i][j] + 1
                if 0 <= r < m and 0 <= c < n and mat[r][c] > z:
                    mat[r][c] = z
                    q.append((r, c))
        return mat