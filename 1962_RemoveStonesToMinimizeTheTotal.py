# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stack = []
        for pile in piles:
            heappush(stack, -pile)
        while k > 0:
            val = -heappop(stack)
            val = val - (val // 2)
            heappush(stack, -val)
            k -= 1
        return -sum(stack)