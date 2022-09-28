# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def minCut(self, s: str) -> int:
        self.palindromeDic = {}
        n = len(s)

        dp = [n - 1 - i for i in range(n)]
        for i in reversed(range(n - 1)):
            if self.isPalindrome(s, i, n - 1):
                dp[i] = 0
                continue
            for j in reversed(range(i, n - 1)):
                if self.isPalindrome(s, i, j):
                    dp[i] = min(dp[i], dp[j + 1] + 1)
        return dp[0]
    
    def isPalindrome(self, s, start, end):
        if start >= end:
            return True
        if (start, end) in self.palindromeDic:
            return self.palindromeDic[(start, end)]
        if s[start] == s[end]:
            self.palindromeDic[(start, end)] = self.isPalindrome(s, start + 1, end - 1)
        else:
            self.palindromeDic[(start, end)] = False
        return self.palindromeDic[(start, end)]