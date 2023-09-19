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

# 2nd solution, TLE
# O(kn) time | O(kn) space
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float("inf") for _ in range(n + 2)] for _ in range(k + 1)]
        dp[0] = [0 for _ in range(n + 2)]

        for i in range(1, k + 1):
            prev = float("inf")
            for j in range(1 + 2 * (i - 1), n + 1):
                dp[i][j] = min(max(dp[i-1][j-2], nums[j - 1]), prev)
                prev = dp[i][j]
        
        return dp[k][n]

# 3rd solution
# O(n log(D)) time | O(1) space
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        while l < r:
            m = (l + r) // 2
            last = take = 0
            for a in nums:
                if last:
                    last = 0
                    continue
                if a <= m:
                    take += 1
                    last = 1
            if take >= k:
                r = m
            else:
                l = m + 1
        return l