# 1st solution
# O(m + n) time | O(1) space
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        ans = 0
        for num in nums1:
            if n & 1:
                ans ^= num
        for num in nums2:
            if m & 1:
                ans ^= num
        return ans