# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minStack = []
        for left, right in intervals:
            if minStack and minStack[0] < left:
                heappop(minStack)
            heappush(minStack, right)
        return len(minStack)