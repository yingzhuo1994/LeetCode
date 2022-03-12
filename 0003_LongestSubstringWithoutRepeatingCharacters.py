# 1st solution
# O(n) time | O(1) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length
