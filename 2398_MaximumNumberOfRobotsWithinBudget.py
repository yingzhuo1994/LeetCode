# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:         
        n = len(chargeTimes)
        start = 0
        runningCost = 0
        timeHeap = []
        for i in range(n):
            while timeHeap and timeHeap[0][1] < start:
                heappop(timeHeap)
            heappush(timeHeap, [-chargeTimes[i], i])
            runningCost += runningCosts[i]
            cost = -timeHeap[0][0] + (i - start + 1) * runningCost
            if cost > budget:
                runningCost -= runningCosts[start]
                start += 1
        return i - start + 1
            