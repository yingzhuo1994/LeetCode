# 1st solution
# O(n) time | O(1) space
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries) - 1):
            delta = timeSeries[i+1] - timeSeries[i]
            ans += min(delta, duration)
        ans += duration
        return ans