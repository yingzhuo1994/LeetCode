# 1st solution, TLE
# O(kn^2) time | O(kn) space
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float("inf") for _ in range(n + 2)] for _ in range(k + 1)]
        dp[0] = [0 for _ in range(n + 2)]
        dp[1] = [float("inf")] + nums + [float("inf")]

        for i in range(2, k + 1):
            for j in range(1 + 2 * (i - 1), n + 1):
                prev = min(dp[i-1][:j-1])
                dp[i][j] = max(prev, nums[j - 1])


        return min(dp[k][1+2*(k-1):-1])