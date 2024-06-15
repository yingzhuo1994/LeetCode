# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            idx = bisect.bisect_right(nums, num + 2 * k)
            ans = max(ans, idx - i)
        return ans

