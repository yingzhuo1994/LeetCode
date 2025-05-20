# 1st solution
# O(n + m * log(m)) time | O(m) space
# where n = len(nums) and m = len(queries)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        events = []
        for l, r in queries:
            events.append([l, -1])
            events.append([r + 1, 1])
        events.sort()
        j = 0
        val = 0
        for i, num in enumerate(nums):
            while j < len(events) and events[j][0] <= i:
                val += events[j][1]
                j += 1
            if num + val > 0:
                return False
        return True