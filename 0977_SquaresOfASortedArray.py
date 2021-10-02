class Solution:
    # O(n) time | O(n) space
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for _ in nums]
        left, right = 0, len(nums) - 1
        k = len(nums) - 1
        while k >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                result[k] = nums[left] * nums[left]
                left += 1
            else:
                result[k] = nums[right] * nums[right]
                right -= 1
            k -= 1
        return result