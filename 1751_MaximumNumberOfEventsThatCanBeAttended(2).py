# 1st solution
# O(kn * log(n)) time | O(kn) space
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda v: [v[1], -v[2], v[0]])
        ends = set([v[1] for v in events])
        ends = [0] + sorted(list(ends))
        ans = 0

        dp = [{end: 0 for end in ends} for _ in range(k + 1)]
        for run in range(1, k + 1):
            for i, (start, end, value) in enumerate(events):
                idx = bisect.bisect_left(ends, start)
                dp[run][end] = max(dp[run][end], dp[run-1][ends[idx - 1]] + value)
                if i > 0:
                    dp[run][end] = max(dp[run][end], dp[run][events[i-1][1]])
                ans = max(ans, dp[run][end])

        return ans

# 2nd solution
# O(kn * log(n)) time | O(n) space
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda v: [v[1], -v[2], v[0]])
        ends = set([v[1] for v in events])
        ends = [0] + sorted(list(ends))
        ans = 0

        dp = {end: 0 for end in ends}
        for run in range(1, k + 1):
            newDp = {end: 0 for end in ends}
            for i, (start, end, value) in enumerate(events):
                idx = bisect.bisect_left(ends, start)
                newDp[end] = max(newDp[end], dp[ends[idx - 1]] + value)
                if i > 0:
                    newDp[end] = max(newDp[end], newDp[events[i-1][1]])
                ans = max(ans, newDp[end])
            dp = newDp

        return ans