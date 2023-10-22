# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minValues = nums[:]
        for i in reversed(range(k)):
            minValues[i] = min(minValues[i + 1], minValues[i])
        for i in range(k + 1, n):
            minValues[i] = min(minValues[i - 1], minValues[i])

        left, right = 0, n - 1
        ans = 0
        while left <= k and right >= k:
            score = min(minValues[left], minValues[right]) * (right - left + 1)
            ans = max(ans, score)
            if minValues[left] <= minValues[right]:
                left += 1
            else:
                right -= 1
        return ans