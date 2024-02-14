# 1st solution
# O(n) time | O(n) space
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = [0 for _ in range(n)]
        even = 0
        odd = 1
        for i in range(n):
            if nums[i] > 0:
                array[even] = nums[i]
                even += 2
            else:
                array[odd] = nums[i]
                odd += 2
        return array