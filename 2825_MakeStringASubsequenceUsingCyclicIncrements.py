# 1st solution
# O(m + n) time | O(1) space
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def isEqual(ch1, ch2):
            if ch1 == ch2:
                return True
            a = ord(ch1) - ord("a") + 1
            b = ord(ch2) - ord("a")
            return a % 26 == b
        m, n = len(str1), len(str2)
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
                if isEqual(str1[i], str2[j]):
                    j += 1
                i += 1
                    
        return j == n