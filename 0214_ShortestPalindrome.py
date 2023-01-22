# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            return s == s[::-1]
        
        n = len(s)
        if n <= 1:
            return s
        i = n
        while not isPalindrome(s[:i]):
            i -= 1
        return s[i:][::-1] + s