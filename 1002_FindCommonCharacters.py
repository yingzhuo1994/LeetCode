# 1st solution
# O(n) time | O(1) space
# where n = len(words) 
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = {ch: 100 for ch in string.ascii_lowercase}
        for word in words:
            cnt = Counter(word)
            for ch in string.ascii_lowercase:
                ans[ch] = min(ans[ch], cnt[ch])
        lst = []
        for k, v in ans.items():
            if v > 0:
                lst += [k] * v
        return lst