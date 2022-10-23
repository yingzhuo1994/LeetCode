# 1st solution
# O(n) time | O(1) space
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        first = 0
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                first = idx + 1
            nums[idx] = -abs(nums[idx])

        second = 0
        for i in range(n):
            if nums[i] > 0:
                second = i + 1

        return [first, second] 