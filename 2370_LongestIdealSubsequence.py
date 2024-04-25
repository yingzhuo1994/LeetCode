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
        dp = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            dp[i] = max(dp[max(0, i - k) : min(25, i + k) + 1]) + 1
        return max(dp)