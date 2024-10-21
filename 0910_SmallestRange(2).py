# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for x, y in pairwise(nums):
            mx = max(x + k, nums[-1] - k)
            mn = min(nums[0] + k, y - k)
            ans = min(ans, mx - mn)
        return ans