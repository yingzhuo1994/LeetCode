# 1st solution
# O(n) time | O(1) space
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        v1 = min(nums1)
        v2 = min(nums2)
        return v2 - v1