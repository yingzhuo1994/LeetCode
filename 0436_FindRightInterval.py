# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        dic = {}
        for i, (a, b) in enumerate(intervals):
            starts.append(a)
            dic[a] = i
        starts.sort()
        ans = []
        for a, b in intervals:
            idx = bisect.bisect_left(starts, b)
            if idx >= len(intervals):
                ans.append(-1)
            else:
                start = starts[idx]
                ans.append(dic[start])
        return ans

# 2nd solution
# O(n*log(n)) time | O(n) space
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for i, (a, b) in enumerate(intervals):
            starts.append([a, i])
        starts.sort()
        ans = []
        for a, b in intervals:
            idx = self.binarySearch(starts, b)
            if idx >= len(intervals):
                ans.append(-1)
            else:
                ans.append(starts[idx][1])
        return ans
    
    def binarySearch(self, starts, target):
        left, right = 0, len(starts)
        while left < right:
            mid = left + (right - left) // 2
            if starts[mid][0] >= target:
                right = mid
            else:
                left = mid + 1
        return left