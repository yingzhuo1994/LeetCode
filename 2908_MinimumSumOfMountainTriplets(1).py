# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        leftNums = [float("inf") for num in nums]
        rightNums = [float(inf) for num in nums]
        minVal = nums[0]
        for i in range(1, len(nums)):
            if minVal < nums[i]:
                leftNums[i] = minVal
            else:
                minVal = nums[i]
        minVal = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            if minVal < nums[i]:
                rightNums[i] = minVal
            else:
                minVal = nums[i]
        ans = float("inf")
        for i in range(1, len(nums) - 1):
            ans = min(ans, leftNums[i] + nums[i] + rightNums[i])
        if ans == float("inf"):
            return -1
        return ans