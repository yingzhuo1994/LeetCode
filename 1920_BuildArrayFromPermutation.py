# 1st solution
# O(n) time | O(n) space
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans