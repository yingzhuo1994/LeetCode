# 1st solution
# O(n) time | O(1) space
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curTime = 0
        totalTime = 0
        n = len(customers)
        for start, duration in customers:
            if curTime <= start:
                totalTime += duration
                curTime = start + duration
            else:
                totalTime += curTime - start + duration
                curTime += duration
        ans = totalTime / n
        return ans