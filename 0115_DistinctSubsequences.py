class Solution:
    # 1st solution, TLE
    # O(2^m) time | O(m) space
    # where m is the length of s
    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        
        count = 0
        for i in range(len(s)):
            if s[i] == t[0]:
                count += self.numDistinct(s[i + 1:], t[1:])
        return count
    
    # 2nd solution, Dynamic Programming
    # O(m * n) time | O(m * n) space
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]
        for j in range(len(s) + 1):
            dp[0][j] = 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]