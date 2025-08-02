# 1st solution
# O(n^3) time | O(n^2) space
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        for a, b, w in edges:
            if w > distanceThreshold:
                continue
            dp[a][b] = w
            dp[b][a] = w
        for i in range(n):
            dp[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        ans = 0
        count = n
        for i in range(n):
            neighbers = len([w for w in dp[i] if w <= distanceThreshold]) - 1
            if neighbers <= count:
                count = neighbers
                ans = i
        return ans