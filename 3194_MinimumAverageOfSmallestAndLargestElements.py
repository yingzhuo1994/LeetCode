# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans = float("inf")
        n = len(nums)
        for i in range(n//2):
            ans = min(ans, nums[i] + nums[n-1-i])
        return ans / 2.0