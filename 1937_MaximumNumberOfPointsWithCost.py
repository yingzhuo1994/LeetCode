# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[float("-inf") for _ in range(n)] for _ in range(m)]
        dp[0] = points[0][:]
        for i in range(1, m):
            left = dp[i-1][:]
            right = dp[i-1][:]
            for j in range(1, n):
                left[j] = max(left[j-1] - 1, left[j])
            for j in reversed(range(n - 1)):
                right[j] = max(right[j + 1] - 1, right[j])
            for j in range(n):
                dp[i][j] = max(left[j], right[j]) + points[i][j]
        return max(dp[-1])

# 2nd solution
# O(mn) time | O(n) space
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0]
        for i in range(1, m):
            left = dp[:]
            right = dp[:]

            for j in range(1, n):
                left[j] = max(left[j-1] - 1, left[j])
            for j in reversed(range(n - 1)):
                right[j] = max(right[j + 1] - 1, right[j])
            for j in range(n):
                dp[j] = max(left[j], right[j]) + points[i][j]
        
        return max(dp)