# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if obstacles[j] <= obstacles[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        mono, res = [], [0] * n
        for i, a in enumerate(obstacles):
            idx = bisect.bisect(mono, a)
            res[i] = idx + 1
            if idx == len(mono):
                mono.append(0)
            mono[idx] = a
        return res