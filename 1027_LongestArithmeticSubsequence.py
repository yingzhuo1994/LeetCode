# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 2
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = max(dp[i].get(diff, 0), dp[j][diff] + 1)
                else:
                    dp[i][diff] = 2
                ans = max(ans, dp[i][diff])
        return ans
        