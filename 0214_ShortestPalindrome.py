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

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        for j in reversed(range(n)):
            if s[i] == s[j]:
                i += 1
        
        if i == n:
            return s
        
        remain = s[i:]
        remain_rev = remain[::-1]
        return remain_rev + self.shortestPalindrome(s[:i]) + remain