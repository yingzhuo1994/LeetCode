# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        rightMaxNums = nums[:]
        for i in reversed(range(len(nums) - 1)):
            rightMaxNums[i] = max(rightMaxNums[i], rightMaxNums[i + 1])
        ans = 0
        a = nums[0]
        for i in range(1, len(nums)):
            ans = max(ans, rightMaxNums[i] - a)
            a = min(a, nums[i])
        return ans if ans > 0 else -1


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        a = nums[0]
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - a)
            a = min(a, nums[i])
        return ans if ans > 0 else -1