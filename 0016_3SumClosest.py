# 1st solution
# O(n^2) time | O(n*log(n)) space
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = float("inf")
        for i in range(len(nums)):
            curTarget = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum < curTarget:
                    left += 1
                elif curSum > curTarget:
                    right -= 1
                else:
                    return target
                if abs(curSum - curTarget) < abs(ans - target):
                    ans = curSum + nums[i]
        return ans
