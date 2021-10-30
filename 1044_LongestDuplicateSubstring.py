class Solution:
    # 1st solution, TLE
    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        while length > 0:
            stringSet = set()
            for i in range(len(s)-length + 1):
                string = s[i:i+length]
                if string in stringSet:
                    return string
                stringSet.add(string)
            length -= 1
        return ""