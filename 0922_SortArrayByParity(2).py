class Solution:
    # 1st solution
    # O(n) time | O(n) space
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        odd = 1
        even = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                result[even] = nums[i]
                even += 2
            else:
                result[odd] = nums[i]
                odd += 2
        return result