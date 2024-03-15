# 1st solution
# O(mn(m+n)) time | O(mn) space
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        pr = {(h, w): p for h, w, p in prices}
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(pr.get((i, j), 0),
                              max((f[i][k] + f[i][j - k] for k in range(1, j)), default=0),  # 垂直切割
                              max((f[k][j] + f[i - k][j] for k in range(1, i)), default=0))  # 水平切割
        return f[m][n]