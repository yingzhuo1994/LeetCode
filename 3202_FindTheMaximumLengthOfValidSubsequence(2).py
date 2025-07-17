# 1st solution
# O(kn) time | O(k) space
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        for m in range(k):
            dp = [0] * k
            for num in nums:
                r = num % k
                dp[r] = dp[m-r] + 1
            ans = max(ans, max(dp))
        return ans