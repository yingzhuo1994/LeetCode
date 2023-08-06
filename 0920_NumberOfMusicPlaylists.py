# 1st solution
# O((L-K)(N-K)) time | O(LN) space
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0 for i in range(goal + 1)] for j in range(n + 1)]

        for i in range(k + 1, n + 1):
            for j in range(i, goal + 1):
                if i == j or i == k + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - k)
        
        return dp[n][goal] % (10**9 + 7)