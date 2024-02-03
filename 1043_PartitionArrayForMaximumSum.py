# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if k == 1:
            return sum(arr)
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