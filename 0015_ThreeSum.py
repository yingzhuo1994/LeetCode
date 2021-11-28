# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            curTarget = target - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > curTarget:
                    right -= 1
                elif nums[left] + nums[right] < curTarget:
                    left += 1
                else:
                    curLst = [nums[i], nums[left], nums[right]]
                    if not result or curLst != result[-1]:
                        result.append(curLst)
                    left += 1
                    right -= 1
        return result