# 1st solution, TLE
# O(n^3) time, O(1) space
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] > nums[k] and abs(nums[i] - nums[j]) < nums[k]:
                        ans += 1
        return ans