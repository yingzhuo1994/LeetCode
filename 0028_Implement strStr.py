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
        if len(needle) > len(haystack):
            return -1
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

# 3rd, KMP solution
# O(n + m) time | O(m) space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        pattern = self.buildPattern(needle)
        return self.doesMatch(haystack, needle, pattern)

    def buildPattern(self, needle):
        pattern = [0 for _ in needle]
        for i in range(1, len(needle)):
            j = pattern[i - 1]
            while j > 0 and needle[i] != needle[j]:
                j = pattern[j - 1]

            if needle[i] == needle[j]:
                j += 1
            pattern[i] = j

        return pattern

    def doesMatch(self, haystack, needle, pattern):
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = pattern[j - 1]

            if haystack[i] == needle[j]:
                j += 1
            
            if j == len(needle):
                return i - len(needle) + 1

        return -1