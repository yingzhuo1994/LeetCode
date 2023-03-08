# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def transform_time(time_str):
            h, m = time_str.split(":")
            return int(h) * 60 + int(m)
        
        lst = [transform_time(time_str) for time_str in timePoints]
        lst.sort()
        ans = 24 * 60
        for i in range(len(lst)):
            if i == len(lst) - 1:
                diff = lst[0] + 24 * 60 - lst[i]
            else:
                diff = lst[i + 1] - lst[i]
            ans = min(ans, diff)
        return ans