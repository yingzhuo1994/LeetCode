class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        k = len(needle)
        n = len(haystack)
        for i in range(n - k + 1):
            if haystack[i:i+k] == needle:
                return i
        return -1
