# 1st solution
# O(n) time | O(n) space
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sumDiff = 0
        for i in range(n):
            sumDiff += abs(nums[i] - nums[0])
        ans = [sumDiff]
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            sumDiff += (2 * i - n) * diff
            ans.append(sumDiff)
        return ans