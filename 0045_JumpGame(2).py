# 1st solution
# O(n) time | O(1) space
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 1
        maxIdx = nums[0]
        curRange = nums[0]
        for i in range(1, len(nums) - 1):
            maxIdx = max(maxIdx, i + nums[i])
            curRange -= 1
            if curRange == 0:
                step += 1
                curRange = maxIdx - i
        return step