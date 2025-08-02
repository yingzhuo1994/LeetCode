# 1st solution
# O(n^2 * k) time | O(kn) space
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1 for _ in range(k + 1)] for _ in range(n)]
        for i in range(1, n):
            num = nums[i]
            for j in range(i):
                if num == nums[j]:
                    for p in range(k + 1):
                        dp[i][p] = max(dp[i][p], dp[j][p] + 1)
                else:
                    for p in range(k):
                        dp[i][p + 1] = max(dp[i][p + 1], dp[j][p] + 1)
        return max(dp[i][k] for i in range(n))