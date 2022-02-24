# 1st brute-force solution
# O(kn) time |  O(k) space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        k = len(needle)
        n = len(haystack)
        for i in range(n - k + 1):
            if haystack[i:i+k] == needle:
                return i
        return -1

# 2nd, KMP solution
# O(n + m) time | O(m) space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        pattern = self.buildPattern(needle)
        return self.doesMatch(haystack, needle, pattern)

    def buildPattern(self, needle):
        pattern = [-1 for _ in needle]
        j = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[j]:
                pattern[i] = j
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1
        return pattern

    def doesMatch(self, haystack, needle, pattern):
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return i - len(needle) + 1
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1
        return -1