# 1st solution
# O(n) time | O(n) space
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[-1] = 1
        MOD = 10**9 + 7
        for i, ch in enumerate(pressedKeys):
            if ch not in ["7", "9"]:
                length = 3
            else:
                length = 4
            for j in reversed(range(i - length, i)):
                if j < -1:
                    continue
                if j >= 0 and pressedKeys[j] != ch:
                    dp[i] += dp[j]
                    break
                dp[i] += dp[j]
            dp[i] %= MOD
        return dp[n - 1]