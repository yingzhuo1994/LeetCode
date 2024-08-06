# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        keys = list(cnt.keys())
        keys.sort(key=lambda v: cnt[v], reverse=True)
        dic = {}
        for i, ch in enumerate(keys):
            dic[ch] = i // 8 + 1
        ans = 0
        for ch in keys:
            ans += cnt[ch] * dic[ch]
        return ans
