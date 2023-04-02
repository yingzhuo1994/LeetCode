class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]
        total = m * n
        for i in range(total):
            x1, y1 = divmod(i, n)
            x2, y2 = divmod(i, c)
            ans[x2][y2] = mat[x1][y1]
        return ans