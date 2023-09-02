# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)
        return dp[-1]

