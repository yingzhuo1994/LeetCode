# 1st solution, TLE
# O(n^2) time | O(1) space
class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        ans = 0
        for length in range(1, n + 1):
            dic = {}
            start = 0
            for i in range(n):
                ch = s[i]
                dic[ch] = dic.get(ch, 0) + 1
                if i - start + 1 > length:
                    dic[s[start]] -= 1
                    if dic[s[start]] == 0:
                        dic.pop(s[start])
                    start += 1
                diff = max(dic.values()) - min(dic.values())
                ans = max(ans, diff)
        return ans