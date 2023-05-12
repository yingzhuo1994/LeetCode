# 1st solution
# O(n) time | O(n) space
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in reversed(range(n)):
            points, brainpower = questions[i]
            dp[i] = max(dp[i+1], dp[min(n, i + brainpower + 1)] + points)
        
        return dp[0]