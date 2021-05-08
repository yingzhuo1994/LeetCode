class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1st recursive solution
        if m == 1 or n == 1:
            return 1
        toRight = self.uniquePaths(m, n - 1)
        toBottom = self.uniquePaths(m - 1, n)
        return toRight + toBottom