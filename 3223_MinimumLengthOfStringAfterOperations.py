# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1
        ans = 0
        for ch in cnt:
            if cnt[ch] & 1:
                ans += 1
            else:
                ans += 2
        return ans