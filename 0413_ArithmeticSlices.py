# 1st solution
# O(n) time | O(1) space
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        count = 0
        diff = nums[1] - nums[0]
        start = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == diff:
                continue
            else:
                length = i - start
                count += (length - 1) * (length - 2) // 2
                start = i - 1
                diff = nums[i] - nums[i - 1]
        if nums[-1] - nums[-2] == nums[-2] - nums[-3]:
            length = len(nums) - start
            count += (length - 1) * (length - 2) // 2
        return count