# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = list(zip(nums2, nums1))
        nums.sort()
        n = len(nums)

        ans = 0
        curSum = 0
        stack = []

        for i in reversed(range(n)):
            while len(stack) > k - 1:
                curSum -= heappop(stack)
            minVal = nums[i][0]
            curSum += nums[i][1]
            heappush(stack, nums[i][1])
            
            if len(stack) == k:
                ans = max(ans, curSum * minVal)
        
        return ans