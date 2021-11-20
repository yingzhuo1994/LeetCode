# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid & 1:
                if nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
        return nums[left]