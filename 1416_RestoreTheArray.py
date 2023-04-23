# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in reversed(range(n)):
            if s[i] == "0":
                continue
            for j in range(i, n):
                left = s[i:j+1]
                left_num = int(left)
                if left_num <= k:
                    dp[i] += dp[j + 1]
                    dp[i] %= MOD
                else:
                    break
        return dp[0]