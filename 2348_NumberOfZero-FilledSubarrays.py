# 1st solution
# O(n) time | O(1) space
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
            if num != 0 or i == len(nums) - 1:
                ans += count * (count + 1) // 2
                count = 0
        return ans  