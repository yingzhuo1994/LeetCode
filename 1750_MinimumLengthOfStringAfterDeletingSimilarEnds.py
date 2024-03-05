# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumLength(self, s: str) -> int:
        start, end = 0, len(s) - 1
        while start < end and s[start] == s[end]:
            i = start
            while i < end and s[i] == s[start]:
                i += 1
            j = end
            while j > start and s[j] == s[end]:
                j -= 1
            if i > j:
                return 0
            start = i
            end = j
        return end - start + 1