# 1st solution
# O(n*log(n)) time | O(1) space
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        minCost = min(costs)
        totalCost = sum(costs)
        if coins < minCost:
            return 0
        elif coins >= totalCost:
            return len(costs)
        heapify(costs)
        count = 0
        while coins >= costs[0]:
            coins -= heappop(costs)
            count += 1
        return count        