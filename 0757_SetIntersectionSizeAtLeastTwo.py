# 1st solution
# O(n * log(⁡n) + nm) time | O(nm) space
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        vals = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            j = intervals[i][0]
            for k in range(len(vals[i]), m):
                ans += 1
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < j:
                        break
                    vals[p].append(j)
                j += 1
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : (x[0], -x[1]))
        ans = 2
        cur, next = intervals[-1][0], intervals[-1][0] + 1
        for xi, yi in reversed(intervals[:-1]):
            if yi >= next:
                continue
            elif yi < cur:
                cur = xi
                next = xi + 1
                ans += 2
            else:
                next = cur
                cur = xi
                ans += 1
        return ans