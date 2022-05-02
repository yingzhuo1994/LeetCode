# O(n) time | O(1) space
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums) - 1
        while even < odd:
            if nums[even] & 1:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd -= 1
            else:
                even += 1
        return nums