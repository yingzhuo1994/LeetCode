class Solution:
    # O(n) time | O(1) space
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if nums[abs(num)] < 0:
                result.append(abs(num))
            nums[abs(num)] *= -1
        return result