# 1st solution, TLE
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        while k > 0:
            value = float("inf")
            idx = -1
            n = min(candidates, len(costs))
            for i in range(n):
                cost = costs[i]
                if cost < value:
                    idx = i
                    value = cost
            for i in range(len(costs) - n, len(costs)):
                cost = costs[i]
                if cost < value:
                    idx = i
                    value = cost

            ans += value
            k -= 1
            costs = costs[:idx] + costs[idx+1:]
        return ans

# 2nd solution
# O((k + m)* log(m) + n) time | O(n) space
# n = len(costs), m = candidates
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        frontHeap = []
        backHeap = []
        n = len(costs)
        visited = [False] * n
        
        for i in range(candidates):
            heappush(frontHeap, [costs[i], i])
            heappush(backHeap, [costs[n-1-i], n-1-i])

        left = candidates
        right = n - 1 - candidates
        ans = 0

        while k > 0:
            if frontHeap[0][0] < backHeap[0][0]:
                value, idx = frontHeap[0]
            elif frontHeap[0][0] > backHeap[0][0]:
                value, idx = backHeap[0]
            else:
                if frontHeap[0][1] <= backHeap[0][1]:
                    value, idx = frontHeap[0]
                else:
                    value, idx = backHeap[0]
            ans += value
            visited[idx] = True
            while frontHeap and visited[frontHeap[0][1]]:
                heappop(frontHeap)
            while backHeap and visited[backHeap[0][1]]:
                heappop(backHeap)
            if idx < left:
                while left < n and visited[left]:
                    left += 1
                if left < n:
                    heappush(frontHeap, [costs[left], left])
                    left += 1
            if idx > right:
                while right >= 0 and visited[right]:
                    right -= 1
                if right >= 0:
                    heappush(backHeap, [costs[right], right])
                    right -= 1
            k -= 1
        
        return ans

# 3rd solution
# O((k + m)* log(m) + n) time | O(n) space
# n = len(costs), m = candidates
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        ans = 0

        pairs = [(value, i) for i, value in enumerate(costs)]
        left, right = min(candidates, n // 2), max(n - candidates, n // 2)
        pq = pairs[:left] + pairs[right:]

        heapify(pq)

        for _ in range(k):
            cost, idx = heappop(pq)
            if idx < left:
                idx, left = left, left + 1
            if idx >= right:
                idx, right = right - 1, right - 1
            if left <= right:
                heappush(pq, pairs[idx])
            
            ans += cost
        
        return ans