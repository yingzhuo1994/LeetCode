# 1st solution
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 先对数组进行排序
        n = len(nums)
        mod = 10 ** 9 + 7
        
        def f(nums, lower_diff):
            # nums 取包含第一项的子序列，使得两两差至少为 lower_diff
            n = len(nums)
            dp = [[0] * k for _ in range(n)]
            dp[0][1] = 1
            for i in range(1, n):
                # 枚举前一项
                for j in range(i):
                    if nums[i] - nums[j] < lower_diff: break
                    # 两项距离不小于 lower_diff 时开始更新
                    for v in range(k - 1):
                        # 结束元素由 j 变成 i
                        # 相当于新增一个长度，v 变为 v + 1
                        dp[i][v+1] += dp[j][v]
                        dp[i][v+1] %= mod
            # 最后统计每个位置结束的数组个数
            ans = [0] * k
            for i in range(n):
                for j in range(k):
                    ans[j] += dp[i][j]
            return ans
        
        ans = 0
        for i in range(n):
            for j in range(i):
                # 枚举最小绝对差
                v = nums[i] - nums[j]
                # 第一个 vs 表示前面的元素和绝对差中小元素的差别
                # 因为这里的最小绝对差取的是最靠前的，因此前面的差不能小于 v + 1
                vs = [nums[j] - nums[idx] for idx in range(j, -1, -1)]
                dp1 = f(vs, v + 1)
                # 第二个 vs 表示前面的元素和绝对差中大元素的差别
                # 后面的差没有限制，只需要不小于 v 即可
                vs = [nums[idx] - nums[i] for idx in range(i, n)]
                dp2 = f(vs, v)
                for x in range(1, k):
                    ans += dp1[x] * dp2[k - x] * v
                    ans %= mod
        return ans

