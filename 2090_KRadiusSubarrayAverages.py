# 1st solution
# O(n) time | O(n) space
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        curSum = 0
        for i in range(n):
            curSum += nums[i]
            if i - 2 * k >= 0:
                ans[i-k] = curSum // (2 * k + 1)
                curSum -= nums[i-2*k]
        
        return ans