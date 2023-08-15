class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        ans = curSum
        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i - k]
            ans = max(ans, curSum)
        return ans / k
