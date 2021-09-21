class Solution:
    # O(n) time | O(1) space
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxLength = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            maxLength = max(maxLength, count)
        return maxLength