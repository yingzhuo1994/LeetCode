# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        keys = list(cnt.keys())
        keys.sort(key=lambda v: cnt[v], reverse=True)
        ans = 0
        for i, ch in enumerate(keys):
            ans += (i // 8 + 1) * cnt[ch]
        return ans
