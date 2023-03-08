# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def transform_time(time_str):
            h, m = time_str.split(":")
            return int(h) * 60 + int(m)
        
        lst1 = [transform_time(time_str) for time_str in timePoints]
        count = collections.Counter(lst1)
        lst2 = []
        for time in count:
            if count[time] > 1:
                return 0
            lst2.append(time + 24 * 60)
        lst = list(count.keys()) + lst2
        lst.sort()
        ans = 24 * 60
        for i in range(len(lst) - 1):
            diff = lst[i + 1] - lst[i]
            ans = min(ans, diff)
        return ans