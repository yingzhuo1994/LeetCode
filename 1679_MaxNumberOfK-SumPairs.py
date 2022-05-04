# O(n*log(n)) time | O(n) space
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            curSum = nums[left] + nums[right]
            if curSum < k:
                left += 1
            elif curSum > k:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1
        return count