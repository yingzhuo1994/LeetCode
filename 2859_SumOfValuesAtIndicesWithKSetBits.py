# 1st solution
# O(n) time | O(1) space
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i, num in enumerate(nums):
            if bin(i)[2:].count("1") == k:
                ans += num
        return ans
