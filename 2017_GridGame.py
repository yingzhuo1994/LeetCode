# 1st solution
# O(n) time | O(n) space
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        curSum = [[0 for _ in range(n + 1)] for _ in range(2)]
        for i in range(n):
            curSum[0][i] = curSum[0][i - 1] + grid[0][i]
            curSum[1][i] = curSum[1][i - 1] + grid[1][i]
        ans = curSum[0][n-1] + curSum[1][n-1]
        for i in range(n):
            a = curSum[1][i-1]
            b = curSum[0][n-1] - curSum[0][i]
            ans = min(ans, max(a, b))
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        total1 = sum(grid[0])
        curSum1 = 0
        curSum2 = 0
        ans = float("inf")
        for i in range(n):
            curSum1 += grid[0][i]
            a = curSum2
            b = total1 - curSum1
            curSum2 += grid[1][i]
            ans = min(ans, max(a, b))
        return ans