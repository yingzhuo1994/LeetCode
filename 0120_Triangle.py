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