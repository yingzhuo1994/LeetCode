# 1st solution
# O(n) time | O(n) space
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0, 0] for _ in range(n + 1)]
        for i, ch in enumerate(s):
            dp[i] = dp[i-1][:]
            if ch == "1":
                dp[i][1] += 1
            else:
                dp[i][0] += 1
        
        ans = n
        for i in range(n):
            front = dp[i-1][1]
            back = dp[n-1][0] - dp[i-1][0]
            count = front + back
            ans = min(ans, count)
        return ans