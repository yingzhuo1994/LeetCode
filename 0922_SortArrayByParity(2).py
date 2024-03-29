# 1st solution
# O(n) time | O(n) space
class Solution:
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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evenIndex = 0
        oddIndex = 1
        while evenIndex < n:
            if nums[evenIndex] & 1:
                nums[oddIndex], nums[evenIndex] = nums[evenIndex], nums[oddIndex]
                oddIndex += 2
            else:
                evenIndex += 2
        return nums