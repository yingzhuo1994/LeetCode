# 1st solution
# O(n) time | O(1) space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
            return intervals
        def getIndex(idx):
            left, right = 0, len(intervals) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if intervals[mid][idx] <= newInterval[idx]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        startIdx = getIndex(0)
        endIdx = getIndex(1)

        if startIdx == len(intervals):
            if intervals[-1][1] < newInterval[0]:
                intervals.append(newInterval)
            else:
                intervals[-1][1] = max(intervals[-1][1], newInterval[1])
        elif endIdx == 0:
            if intervals[0][0] > newInterval[1]:
                intervals.insert(0, newInterval)
            else:
                intervals[0][0] = min(intervals[0][0], newInterval[0])
        else:
            if startIdx > 0 and intervals[startIdx - 1][1] >= newInterval[0]:
                start = startIdx - 1
            else:
                start = startIdx
            startValue = min(intervals[start][0], newInterval[0])
            
            if endIdx < len(intervals) and intervals[endIdx][0] > newInterval[1]:
                end = endIdx - 1
            else:
                end = min(endIdx, len(intervals) - 1)
            endValue = max(intervals[end][1], newInterval[1])
        
            for i in reversed(range(start, end + 1)):
                intervals.pop(i)
            intervals.insert(start, [startValue, endValue])
        return intervals

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < newInterval[0]:
                res.append([x, y])
            elif newInterval[1] < x:
                i -= 1
                break
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
                
        return res + [newInterval] + intervals[i+1:]