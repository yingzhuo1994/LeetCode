# 1st solution
# O(n) time | O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1 for _ in range(len(nums))]
        rightProduct = [1 for _ in range(len(nums))]
        result = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1]
        
        for i in reversed(range(len(nums) - 1)):
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            result[i] = leftProduct[i] * rightProduct[i]
        
        return result

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        leftRunningProduct = 1
        for i in range(len(nums)):
            result[i] = leftRunningProduct
            leftRunningProduct *= nums[i]
        
        rightRunningProduct = 1
        for i in reversed(range(len(nums))):
            result[i] *= rightRunningProduct
            rightRunningProduct *= nums[i]
                
        return result