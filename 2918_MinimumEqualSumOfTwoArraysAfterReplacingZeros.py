# 1st solution
# O(m + n) time | O(1) space
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        sum1 = sum(nums1)
        min1 = sum1 + zero1
        sum2 = sum(nums2)
        min2 = sum2 + zero2

        if zero1 == 0 and sum1 < min2:
            return -1
        if zero2 == 0 and sum2 < min1:
            return -1

        if min1 >= min2:
            return min1
        elif min2 >= min1:
            return min2
        
