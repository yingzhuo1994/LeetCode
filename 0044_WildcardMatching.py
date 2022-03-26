# 1st solution
# O(mn) time | O(mn) space
# where m, n are the length of s and p, separately.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]

# 2nd solution
# O(mn) time | O(n) space
# where m, n are the length of s and p, separately.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False for j in range(len(p) + 1)]
        dp[0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                break
            dp[j] = True
        for i in range(1, len(s) + 1):
            cur = [False for j in range(len(p) + 1)]
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    cur[j] = dp[j] or cur[j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    cur[j] = dp[j - 1]
            dp = cur
        return dp[-1]