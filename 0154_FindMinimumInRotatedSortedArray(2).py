class Solution:
    # 1st solution
    # O(log(n)) time | O(1) space
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] < nums[right]:
                return nums[left]
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left += 1
        return nums[left]