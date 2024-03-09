# 1st solution
# O(n * log(n) + k * log(U)) time | O(min(k, n)) space
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        s = 0
        for i, x in enumerate(nums):
            if x >= 0:
                s += x
            else:
                nums[i] = -x
        nums.sort()

        def check(sum_limit: int) -> bool:
            cnt = 1  # 空子序列算一个
            def dfs(i: int, s: int) -> None:
                nonlocal cnt
                if cnt == k or i == len(nums) or s + nums[i] > sum_limit:
                    return
                cnt += 1  # s + nums[i] <= sum_limit
                dfs(i + 1, s + nums[i])  # 选
                dfs(i + 1, s)  # 不选
            dfs(0, 0)
            return cnt == k  # 找到 k 个元素和不超过 sum_limit 的子序列
        return s - bisect_left(range(sum(nums)), True, key=check)