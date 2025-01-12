# 1st solution
# O(n) time | O(1) space
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1
        odd = 0
        for ch in cnt:
            if cnt[ch] & 1:
                odd += 1
        if len(s) < k or odd > k:
            return False
        return True