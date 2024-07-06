# 1st solution
# O(n) time | O(1) space
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        prev = -1
        start = 0
        ans = 0
        for i, num in enumerate(nums):
            if num != prev:
                ans += i - start + 1
            else:
                ans += 1
                start = i
            prev = num
        return ans