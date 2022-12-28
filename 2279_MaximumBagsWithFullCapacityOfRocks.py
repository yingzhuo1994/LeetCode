# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        leftRocks = additionalRocks
        n = len(capacity)
        stack = []
        for rock, cap in zip(rocks, capacity):
            diff = cap - rock
            if diff > 0:
                heappush(stack, diff)
        while stack and leftRocks > 0:
            diff = heappop(stack)
            if leftRocks >= diff:
                leftRocks -= diff
            else:
                diff -= leftRocks
                leftRocks = 0
                heappush(stack, diff)
        return n - len(stack)