# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dic = {ch: 0 for ch in string.ascii_lowercase}
        n = len(s)
        for i in range(n):
            val = dic[s[i]]
            for ch in dic:
                if abs(ord(ch) - ord(s[i])) <= k:
                    val = max(val, dic[ch] + 1)
            dic[s[i]] = val
        return max(dic.values())

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dic = {ch: 0 for ch in string.ascii_lowercase}
        n = len(s)
        for i in range(n):
            val = dic[s[i]]
            for j in range(max(ord("a"), ord(s[i]) - k), min(ord("z"), ord(s[i]) + k) + 1):
                val = max(val, dic[chr(j)] + 1)
            dic[s[i]] = val
        return max(dic.values())