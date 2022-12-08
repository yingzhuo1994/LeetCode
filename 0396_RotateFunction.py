# 1st solution
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        def f(nums, k):
            array = nums[k:] + nums[:k]
            ans = 0
            for i, num in enumerate(array):
                ans += i * num
            return ans
        
        maxSum = float("-inf")
        for i in range(len(nums)):
            maxSum = max(maxSum, f(nums, i))
        return maxSum