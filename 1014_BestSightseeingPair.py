# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0] * n
        dp[0] = values[0]
        v = values[0]
        for i in range(1, n):
            v -= 1
            dp[i] = v + values[i]
            if values[i] > v:
                v = values[i]
        
        return max(dp[1:]) 