# 1st solution
# O(k * n^2) | O(kn) space
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        n = len(nums)
        if k == 1:
            return prefixSum[-1] / n
        elif k == n:
            return prefixSum[-1]
        dp = [[-1 for _ in range(n)] for _ in range(k)]
        for end in range(n):
            dp[0][end] = prefixSum[end + 1] / (end + 1)
        for m in range(1, k):
            for start in range(m, n):
                prev = dp[m - 1][start - 1]
                for end in range(start, n):
                    val = (prefixSum[end + 1] - prefixSum[start]) / (end - start + 1)
                    dp[m][end] = max(dp[m][end], prev + val)
        return dp[-1][-1]
