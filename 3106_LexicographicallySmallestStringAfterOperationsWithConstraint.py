# 1st solution
# O(13^n) time | O(n) space
# where n = len(s)
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def getDist(a, b):
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)
        
        def dfs(idx, t):
            if idx == len(s):
                return ""
            if t == 0:
                return s[idx:]
            if s[idx] == "a":
                return "a" + dfs(idx + 1, t)
            for ch in string.ascii_lowercase:
                cost = getDist(ch, s[idx])
                if cost <= t:
                    return ch + dfs(idx + 1, t-cost)
        return dfs(0, k)