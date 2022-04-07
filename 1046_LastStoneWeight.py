# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stack = []
        for stone in stones:
            heapq.heappush(stack, -stone)
        
        while len(stack) > 1:
            y = -heapq.heappop(stack)
            x = -heapq.heappop(stack)
            if x != y:
                y -= x
                heapq.heappush(stack, -y)
        return -stack[0] if stack else 0
        