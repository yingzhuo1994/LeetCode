# 1st solution
# O(1) time | O(1) space
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        for i in range(n + 1):
            k = len(bin(i)) - 2
            new = "0" * (n - k) + bin(i)[2:]
            if new not in nums:
                return new