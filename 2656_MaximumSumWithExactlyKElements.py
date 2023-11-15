# 1st solution
# O(n) time | O(1) space
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        return (maxNum + maxNum + k - 1) * k // 2