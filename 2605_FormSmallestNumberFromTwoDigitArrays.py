# 1st solution
# O(1) time | O(1) space 
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        common = nums1 & nums2
        if common:
            return min(common)
        
        a = min(nums1)
        b = min(nums2)
        if a > b:
            a, b = b, a
        
        if a != 0:
            return a * 10 + b
        else:
            return b * 10 + a