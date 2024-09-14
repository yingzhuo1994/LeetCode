# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 0
        count = 0
        ans = 1
        for num in nums:
            if num > k:
                k = num
                count = 1
                ans = 1
            elif num < k:
                count = 0
            else:
                count += 1
            ans = max(ans, count)
        return ans