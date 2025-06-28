# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx = sorted(range(len(nums)), key=lambda i: nums[i])  # 创建下标数组，对下标数组排序
        idx = sorted(idx[-k:])  # 取前 k 大元素的下标，排序
        return [nums[i] for i in idx]  # 取出 nums 的子序列