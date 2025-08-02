# 1st solution
# O(n) time | O(1) space
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        for hour in hours:
            r = hour % 24
            cnt[r] += 1
        ans = 0
        for h in range(1, 12):
            k = 24 - h
            ans += cnt[h] * cnt[k]
        ans += cnt[0] * (cnt[0] - 1) // 2 + cnt[12] * (cnt[12] - 1) // 2
        return ans