# 1st solution
# O(n) time | O(n) space
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        for i in reversed(range(n - 1)):
            stoneValue[i] += stoneValue[i + 1]
        
        @cache
        def dfs(idx):
            if idx >= n:
                return 0
            ans = float("-inf")
            for k in range(1, 4):
                ans = max(ans, stoneValue[idx] - dfs(idx + k))
            return ans
        
        Alice = dfs(0)
        Bob = stoneValue[0] - Alice

        if Alice > Bob:
            return "Alice"
        elif Alice < Bob:
            return "Bob"
        else:
            return "Tie"

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 3
        n = len(stoneValue)
        for i in reversed(range(n)):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"