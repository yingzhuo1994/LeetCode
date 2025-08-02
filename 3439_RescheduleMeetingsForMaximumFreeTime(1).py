# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0
        gap = 0
        startTime.append(eventTime)
        endTime.append(0)
        for i in range(k + 1):
            gap += startTime[i] - endTime[i-1]
        ans = gap
        for i in range(k + 1, len(startTime)):
            gap += startTime[i] - endTime[i - 1] - (startTime[i - k - 1] - endTime[i - k - 2])
            ans = max(ans, gap)
        return ans