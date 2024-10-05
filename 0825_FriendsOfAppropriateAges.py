# 1st solution
# O(n) time | O(1) space
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = Counter(ages)
        keys = list(cnt.keys())
        ans = 0
        n = len(keys)
        for i in range(n):
            x = keys[i]
            for j in range(n):
                y = keys[j]
                if y <= 0.5 * x + 7 or y > x or y > 100 and x < 100:
                    continue
                if i == j:
                    continue
                else:
                    ans += cnt[x] * cnt[y]
        for i in range(n):
            x = keys[i]
            y = x
            if y <= 0.5 * x + 7 or y > x or y > 100 and x < 100:
                continue
            ans += cnt[x] * (cnt[x] - 1)
        return ans

