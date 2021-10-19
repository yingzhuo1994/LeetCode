class Solution:
    # 1st solution
    # O(n^2) time | O(n) space
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1 for _ in nums1]
        for i in range(len(nums1)):
            state = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    state = True
                if nums1[i] < nums2[j] and state:
                    result[i] = nums2[j]
                    break
        return result