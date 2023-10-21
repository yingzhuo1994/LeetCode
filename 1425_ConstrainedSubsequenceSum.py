# 1st solution
# O(nk) time | O(n + k) space
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + k)]
        for i in range(n):
            value = 0
            for j in range(i - k, i):
                value = max(value, dp[j])
            dp[i] = value + nums[i]
        return max(dp[:-k])

# 2nd solution
# O(nlog(n)) time | O(n) space
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        minHeap = []
        ans = float("-inf")
        for i, num in enumerate(nums):
            while minHeap and i - minHeap[0][1] > k:
                heappop(minHeap)
            value = num
            if minHeap and minHeap[0][0] < 0:
                value = -minHeap[0][0] + num

            heappush(minHeap, [-value, i])
            ans = max(ans, value)
        return ans