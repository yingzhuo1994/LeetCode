# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n // 2):
            curSum = nums[i] + nums[n - 1 - i]
            ans = max(ans, curSum)
        return ans