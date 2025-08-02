# 1st solution
# O(n) time | O(1) space
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            if (nums[i] ^ nums[i + 1]) & 1:
                continue
            return False
        return True