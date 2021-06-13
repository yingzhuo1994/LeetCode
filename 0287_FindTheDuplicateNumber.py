class Solution:
    # 1st solution
    # O(n) time | O(1) space
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        for i in range(len(nums)):
            value = abs(nums[i])
            if nums[value - 1] < 0:
                duplicate = value
                break
            else:
                nums[value - 1] *= -1
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return duplicate