# 1st solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if s and p[0] in {s[0], '.'}:
            first_match = True
        else:
            first_match = False
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# 2nd solution, Top-Down
# O(TP) time | O(TP) space
# where T, P are the lengths of the s and p respectively.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

# 3rd solution, Bottom-Up
# O(TP) time | O(TP) space
# where T, P are the lengths of the s and p respectively.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]

# 4th solution, Bottom-Up
# O(TP) time | O(TP) space
# where T, P are the lengths of the s and p respectively.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:       
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, len(p) + 1):
            dp[0][j] = p[j-1] == '*' and dp[0][j-2]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in {s[i - 1], '.'}: 
                    dp[i][j] = dp[i-1][j-1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j-2] or (p[j - 2] in {s[i - 1], "."} and dp[i-1][j])
        return dp[-1][-1]