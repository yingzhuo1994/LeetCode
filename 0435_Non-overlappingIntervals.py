# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda v: [v[1], v[0]])

        n = len(intervals)
        start = 0
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[start][1]:
                count += 1
                start = i

        return n - count

# 2nd solution
# O(n*log(n)) time | O(n) space
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start = 0
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[start][1] <= intervals[i][0]:
                start = i
            else:
                ans += 1
                if intervals[start][1] > intervals[i][1]:
                    start = i
        return ans