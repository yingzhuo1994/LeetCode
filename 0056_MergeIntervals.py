class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) time | O(n) space
        intervals.sort()
        lst = [intervals[0]]
        for i in range(1, len(intervals)):
            curInterval = intervals[i]
            if curInterval[0] > lst[-1][1]:
                lst.append(curInterval)
            elif curInterval[1] > lst[-1][1]:
                lst[-1][1] = curInterval[1]
        return lst
