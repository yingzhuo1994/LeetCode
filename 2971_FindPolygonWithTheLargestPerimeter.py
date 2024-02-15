# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        preSum = nums[0] + nums[1]
        for i in range(2, n):
            if preSum > nums[i]:
                ans = max(ans, preSum + nums[i])
            preSum += nums[i]
        return ans