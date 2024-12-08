# 1st solution
# O(n * log(n)) time | O(n) time
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda v: [v[1], v[0], v[2]])
        n = len(events)
        time = [0]
        dic = {0: 0}
        ans = 0
        for start, end, value in events:
            idx = bisect.bisect_left(time, start) - 1
            ans = max(ans, dic[time[idx]] + value)
            if end not in dic:
                dic[end] = max(dic[time[-1]], value)
                time.append(end)
            else:
                dic[end] = max(dic[end], value)
        return ans
