# 1st solution, TLE
# O(k * maxPts) time | O(k + maxPts) space
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        total = k + maxPts
        dp = [0] * (total)
        dp[0] = 1
        for i in range(k):
            for j in range(1, maxPts + 1):
                dp[i + j] += dp[i] * 1 / maxPts

        return sum(dp[k:n+1])

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts: 
            return 1
        dp = [1.0] + [0.0] * n
        Wsum = 1.0
        for i in range(1, n + 1):
            dp[i] = Wsum / maxPts
            if i < k: 
                Wsum += dp[i]
            if i - maxPts >= 0: 
                Wsum -= dp[i - maxPts]
        
        return sum(dp[k:])