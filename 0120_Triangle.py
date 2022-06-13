# 1st solution, bottom-up dp
# O(n) time | O(n) space
# where n is the element number of triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[value for value in layer] for layer in triangle]
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]

# 2nd solution, top-down dp
# O(n) time | O(n) space
# where n is the element number of triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float("inf") for _ in layer] for layer in triangle]
        dp[0] = triangle[0]
        for i in range(1, len(triangle)):
            for k in range(len(triangle[i-1])):
                dp[i][k] = min(dp[i][k], dp[i-1][k] + triangle[i][k])
                dp[i][k+1] = min(dp[i][k+1], dp[i-1][k] + triangle[i][k+1])
        return min(dp[-1])