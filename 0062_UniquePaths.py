class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1st recursive solution
        # O(mn) time | O(m + n) space
        if m == 1 or n == 1:
            return 1
        toRight = self.uniquePaths(m, n - 1)
        toBottom = self.uniquePaths(m - 1, n)
        return toRight + toBottom

        # 2nd iterative solution
        # O(mn) time | O(n) space 
        ways = [1 for _ in range(n)]
        for i in range(m - 1):
            for j in reversed(range(n - 1)):
                ways[j] = ways[j] + ways[j + 1]
        return ways[0]

