# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
        return nums