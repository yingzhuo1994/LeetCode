class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1st brute-force solution
        # O(kn) time |  O(k) space
        if needle == "":
            return 0
        k = len(needle)
        n = len(haystack)
        for i in range(n - k + 1):
            if haystack[i:i+k] == needle:
                return i
        return -1
