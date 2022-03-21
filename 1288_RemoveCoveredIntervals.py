# 1st solution
# O(nlog(n)) time | O(n) space
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        right, count = -1, 0
        for _, end in intervals:
            if end > right:
                count += 1
                right = end
        return count