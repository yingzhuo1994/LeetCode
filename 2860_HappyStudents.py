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

# 3rd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[0] > 0  # 一个学生都不选
        for i, (x, y) in enumerate(pairwise(nums), 1):
            if x < i < y:
                ans += 1
        return ans + 1  # 一定可以都选
