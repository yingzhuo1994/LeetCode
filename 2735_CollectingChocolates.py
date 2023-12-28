# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        ans = float("inf")
        n = len(nums)
        dp = nums[:]
        for i in range(n):
            cost = sum(dp) + i * x
            ans = min(ans, cost)
            new = dp[:]
            for i in range(n):
                idx = (i + 1) % n
                new[idx] = min(new[idx], dp[i])
            dp = new
        return ans