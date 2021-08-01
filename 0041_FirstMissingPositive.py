class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = 1
        while k in nums:
            k += 1
        return k