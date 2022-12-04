# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        idx = 0
        ans = float("inf")
        for i in range(n):
            front = nums[i] // (i + 1)
            back = (nums[-1] - nums[i]) // (n - i - 1) if i != n - 1 else 0
            diff = abs(front - back)
            if diff < ans:
                ans = diff
                idx = i
        return idx
            