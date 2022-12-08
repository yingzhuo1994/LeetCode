# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        def f(nums, k):
            array = nums[k:] + nums[:k]
            ans = 0
            for i, num in enumerate(array):
                ans += i * num
            return ans
        
        fk = f(nums, 0)
        s = sum(nums)
        n = len(nums)
        
        maxSum = fk
        for i in range(1, n):
            fk += s - n * nums[n - i]
            maxSum = max(maxSum, fk)

        return maxSum