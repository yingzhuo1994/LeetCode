# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def maximumLength(self, s: str) -> int:
        dic = {}
        start = -1
        last = None
        for i, ch in enumerate(s):
            if ch != last:
                start = i
                last = ch
            sub = s[start:i+1]
            if sub in dic:
                continue
            dic[sub] = 1
            for j in range(i - len(sub) + 2, len(s) - len(sub) + 1):
                if s[j:j+len(sub)] == sub:
                    dic[sub] += 1
        return max([len(sub) for sub in dic if dic[sub] >= 3] + [-1])
      