# 1st solution
# O(n * log(n)) time | O(1) space
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        lst = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == "I":
                lst[i + 1] = max(lst[i] + 1, lst[i + 1])
            else:
                lst[i] = max(lst[i], lst[i + 1] + 1)
        
        for i in reversed(range(n)):
            if s[i] == "I":
                lst[i + 1] = max(lst[i] + 1, lst[i + 1])
            else:
                lst[i] = max(lst[i], lst[i + 1] + 1)
        
        ranks = sorted([[val, i] for i, val in enumerate(lst)])
        ans = [0] * (n + 1)
        v = 0
        for val, i in ranks:
            ans[i] = v
            v += 1
        return ans