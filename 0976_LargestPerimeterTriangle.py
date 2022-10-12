# 1st solution
# O(n^2 * log(n)) time | O(n) space
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            for j in reversed(range(i + 1, n - 1)):
                curSum = nums[i] + nums[j]
                k = bisect.bisect_left(nums, curSum) - 1
                if k > j:
                    ans = max(ans, curSum + nums[k])
                    break
        return ans