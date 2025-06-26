# 1st solution
# O(n) time | O(n) space
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n, m = len(s), k.bit_length()
        if n < m:  # int(s, 2) < k
            return n  # 全选
        ans = m if int(s[-m:], 2) <= k else m - 1  # 后缀长度
        return ans + s[:-m].count('0')  # 添加前导零