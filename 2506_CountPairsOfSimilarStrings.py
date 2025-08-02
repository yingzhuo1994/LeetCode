# 1st solution
# O(n) time | O(n) space
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = Counter()
        for word in words:
            unique = set(list(word))
            key = "".join(sorted(list(unique)))
            cnt[key] += 1
        ans = 0
        for v in cnt.values():
            ans += v * (v - 1) // 2
        return ans