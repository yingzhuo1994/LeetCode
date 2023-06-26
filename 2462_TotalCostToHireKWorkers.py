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