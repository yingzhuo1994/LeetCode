class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1st solution
        # O(n) time | O(n) space
        if not s:
            return 0
        p1, p2 = 0, 0
        pair = [0, 0]
        while p2 < len(s):
            ch = s[p2]
            if ch in s[p1:p2]:
                p1 += 1
            else:
                if p2 - p1 > pair[1] - pair[0]:
                    pair = [p1, p2]
                p2 += 1
        return pair[1] - pair[0] + 1
