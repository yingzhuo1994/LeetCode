# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s_rev = s[::-1]
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        ans = 1

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                ans = max(ans, dp[i][j])
        
        return ans