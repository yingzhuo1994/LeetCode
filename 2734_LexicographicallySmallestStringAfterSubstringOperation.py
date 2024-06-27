# 1st solution
# O(n) time | O(n) space
class Solution:
    def smallestString(self, s: str) -> str:
        start = 0
        while start < len(s) and s[start] == "a":
            start += 1
        if start == len(s):
            return s[:-1] + "z"
        end = start
        while end < len(s) and s[end] != "a":
            end += 1
        def getPrevChar(ch):
            diff = ord(ch) - ord("a")
            diff += 25
            diff %= 26
            return chr(ord("a") + diff)

        t = "".join([getPrevChar(s[i]) for i in range(start, end)])
        return s[:start] + t + s[end:]