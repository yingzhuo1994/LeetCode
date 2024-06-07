# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        for i in range(3, len(nums), 2):
            if nums[i - 1] + nums[i] != score:
                return i // 2
        return len(nums) // 2