# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0 + nums[0] != 0
        idx = 0
        while idx < n:
            target = nums[idx] + 1
            while idx < n and nums[idx] < target:
                idx += 1
            if idx > nums[idx - 1] and (idx == n or nums[idx] > idx):
                ans += 1
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0 + nums[0] != 0
        idx = 0
        while idx < n:
            idx = bisect.bisect_left(nums, nums[idx] + 1)
            if idx > nums[idx - 1] and (idx == n or nums[idx] > idx):
                ans += 1
        return ans