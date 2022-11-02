# 1st solution
# O(32n) time | O(1) space
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for k in range(32):
            count = 0
            for num in nums:
                count += (num >> k) & 1
            ans += count * (n - count)
        return ans