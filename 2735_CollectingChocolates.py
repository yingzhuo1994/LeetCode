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

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = list(range(0, n * x, x))  # s[k] 统计操作 k 次的总成本
        for i, mn in enumerate(nums):  # 子数组左端点
            for j in range(i, n + i):  # 子数组右端点（把数组视作环形的）
                mn = min(mn, nums[j % n])  # 维护从 nums[i] 到 nums[j] 的最小值
                s[j - i] += mn  # 累加操作 j-i 次的花费
        return min(s)