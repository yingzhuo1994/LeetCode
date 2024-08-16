# 1st solution
# O(nm * log(U)) time | O(nm * log(U))
# where U = MAX(nums) <= 10^5
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)
        @cache
        def dfs(i: int, j: int, and_: int) -> int:
            if n - i < m - j:  # 剩余元素不足
                return inf
            if j == m:  # 分了 m 段
                return 0 if i == n else inf
            and_ &= nums[i]
            res = dfs(i + 1, j, and_)  # 不划分
            if and_ == andValues[j]:  # 划分，nums[i] 是这一段的最后一个数
                res = min(res, dfs(i + 1, j + 1, -1) + nums[i])
            return res
        ans = dfs(0, 0, -1)
        return ans if ans < inf else -1