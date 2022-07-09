# 1st solution
# O(nk) time | O(n) space
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float("-inf") for _ in range(n)]
        dp[0] = nums[0]
        for i in range(n):
            for j in range(1, k + 1):
                if i + j < n:
                    dp[i+j] = max(dp[i+j], dp[i] + nums[i+j])               
                else:
                    break
        return dp[-1]

# 2nd solution
# O(n * log(k)) time | O(k) space
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minHeap = [[-nums[0], 0]]
        ans = nums[0]
        for i in range(1, n):
            while minHeap[0][1] < i - k:
                heapq.heappop(minHeap)
            
            newSum = minHeap[0][0] - nums[i]
            heapq.heappush(minHeap, [newSum, i])
            ans = -newSum
        return ans