# 1st solution
# O(n) time | O(n) space
class Solution:
    def numDecodings(self, s: str) -> int:    
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n):
            if s[i] != "0":
                dp[i] += dp[i-1]
                if i + 1 < n and int(s[i:i+2]) <= 26:
                    dp[i+1] += dp[i-1]
        return dp[-2]


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        front, back = 1, 1
        for i in range(1, len(s)):
            single, double = 0, 0
            if int(s[i]) > 0:
                single = 1
            if 10 <= int(s[i-1:i+1]) <= 26:
                double = 1
            if single or double:
                cur = back * single + front * double
                front, back = back, cur
            else:
                return 0
        return back