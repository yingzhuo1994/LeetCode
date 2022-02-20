# 1st solution
# O(nlog(n)) time | O(n) space
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda v: v[0])
        stack = []
        for i in range(len(intervals)):
            isCoveredResult = False
            for j in range(len(stack)):
                if self.isCovered(stack[j], intervals[i]):
                    isCoveredResult = True
                    break
                elif self.isCovered(intervals[i], stack[j]):
                    stack[j] = intervals[i]
                    isCoveredResult = True
                    break
            if isCoveredResult:
                continue
            else:
                stack.append(intervals[i])
        return len(stack)
   
    def isCovered(self, one, two):
        return one[0] <= two[0] and two[1] <= one[1]