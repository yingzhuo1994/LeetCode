# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            num = nums[i]
            lo = bisect.bisect_left(nums, lower - num)
            if lo >= i:
                continue
            hi = bisect.bisect_right(nums, upper - num, hi=i) - 1
            count = hi - lo + 1
            if count >= 0:
                ans += count
        return ans