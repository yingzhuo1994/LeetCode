# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = sum(nums)
        ans = nums[0]
        n = len(nums)
        for i in reversed(range(1, n)):
            target = (total + i) // (i + 1)
            if nums[i] >= target:
                ans = max(ans, target)
                total -= target
                nums[i-1] += nums[i] - target
            else:
                total -= nums[i]
        return ans