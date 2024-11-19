# 1st solution
# O(n) time | O(k) space
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        ans = 0
        n = len(nums)
        curSum = 0
        for i in range(k - 1):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            curSum += nums[i]
        for i in range(k - 1, n):
            curSum += nums[i]
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            if len(dic) == k:
                ans = max(ans, curSum)
            dic[nums[i-k+1]] -= 1
            curSum -= nums[i-k+1]
            if dic[nums[i-k+1]] == 0:
                del dic[nums[i-k+1]]
        return ans