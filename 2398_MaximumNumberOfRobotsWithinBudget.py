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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = s = left = 0
        q = deque()
        for right, (t, c) in enumerate(zip(chargeTimes, runningCosts)):
            # 1. 入
            while q and t >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right)
            s += c  # 维护 sum(runningCosts)

            # 2. 出
            while q and chargeTimes[q[0]] + (right - left + 1) * s > budget:
                if q[0] == left:
                    q.popleft()
                s -= runningCosts[left]  # 维护 sum(runningCosts)
                left += 1

            # 3. 更新答案
            ans = max(ans, right - left + 1)
        return ans