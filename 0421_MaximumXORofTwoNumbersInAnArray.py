# 1st solution, brute-force
# O(n^2) time | O(1) space
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        largest = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i] ^ nums[j]
                largest = max(largest, x)
        return largest