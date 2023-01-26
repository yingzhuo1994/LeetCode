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

# 3rd solution, KMP
# O(n) time | O(n) space
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)
        f = [0] * n_new
        for i in range(1, n_new):
            t = f[i - 1]
            while t > 0 and s_new[i] != s_new[t]:
                t = f[t - 1]

            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t

        return rev[0:n - f[n_new - 1]] + s