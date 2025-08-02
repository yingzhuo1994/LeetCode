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


# 2nd solution
# O(n * log(n)) time | O(n) time
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        proc = []
        ans = m = 0  # m represents max value of finished event so far
        for s,e,v in events:
            proc.append( (s, True, v) )     # time, is_start, val
            proc.append( (e+1, False, v) )  # use e+1 (inclusive)
        proc.sort()  # sort by time
        
        for time, is_start, val in proc:
            if is_start:
                ans = max(ans, m+val)
            else:
                m = max(m, val)
        return ans