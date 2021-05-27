class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 1st brute-force solution
        largest = nums[0]
        for i in range(len(nums)):
            curProduct = 1
            for j in range(i, len(nums)):
                curProduct *= nums[j]
                largest = max(largest, curProduct)
        return largest

