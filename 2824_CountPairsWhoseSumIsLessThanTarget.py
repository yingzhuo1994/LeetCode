# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                curSum = nums[i] + nums[j]
                if curSum < target:
                    ans += 1
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in reversed(range(1, n)):
            curTarget = target - nums[i]
            idx = bisect.bisect_left(nums, curTarget, hi=i)
            ans += idx
        return ans