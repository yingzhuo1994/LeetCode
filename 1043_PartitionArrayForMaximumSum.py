# 1st solution
# O(kn) time | O(n) space
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dfs(idx):
            if idx == len(arr):
                return 0
            maxVal = 0
            maxSum = 0
            for i in range(idx, min(idx + k, len(arr))):
                maxVal = max(maxVal, arr[i])
                maxSum = max(maxSum, maxVal * (i - idx + 1) + dfs(i + 1))
            return maxSum

        return dfs(0)

# 2nd solution
# O(kn) time | O(n) space
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            curMax = 0
            for j in range(1, min(k, i) + 1):
                curMax = max(curMax, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + curMax * j)
        return dp[n]