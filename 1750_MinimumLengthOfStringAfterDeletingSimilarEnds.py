# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumLength(self, s: str) -> int:
        start, end = 0, len(s) - 1
        while start < end and s[start] == s[end]:
            ch = s[start]
            while start < end and s[start] == ch:
                start += 1
            while end >= start and s[end] == ch:
                end -= 1
        return end - start + 1