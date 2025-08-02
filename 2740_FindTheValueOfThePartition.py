# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[-1]
        n = len(nums)
        for i in range(n - 1):
            ans = min(ans, nums[i+1] - nums[i])
        return ans