# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [[max(i - ranges[i], 0), min(i + ranges[i], n)] for i in range(n + 1) if ranges[i] > 0]
        intervals.sort()
        print(intervals)

        left, right = 0, 0
        count = 1
        for a, b in intervals:
            if b <= right:
                continue
            elif a <= left:
                right = b
            elif a <= right:
                left, right = right, b
                count += 1
            else:
                return -1
        
        if right < n:
            return -1
        return count
