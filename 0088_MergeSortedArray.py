class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n -1
        while k >= 0 and i >= 0 and j >= 0:
            a = nums1[i]
            b = nums2[j]
            if a > b:
                nums1[k] = a
                i -= 1
            else:
                nums1[k] = b
                j -= 1
            k -= 1
        if i < 0:
            nums1[:j+1] = nums2[:j+1]
        return nums1
