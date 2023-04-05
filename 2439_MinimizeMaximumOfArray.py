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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            ans = max(ans, (nums[i] + i) // (i + 1))
        return ans