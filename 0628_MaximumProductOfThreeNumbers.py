# 1st solution, TLE
# O(n^3) time | O(1) space
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans = max(ans, nums[i] * nums[j] * nums[k])
        return ans
