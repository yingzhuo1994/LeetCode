# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda v: [v[0], -v[1]])
        ans = 0
        last = 0
        for start, end in meetings:
            if last < start:
                ans += start - last - 1
            last = max(last, end)
        ans += days - last
        return ans