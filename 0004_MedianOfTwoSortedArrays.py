class Solution:
    # 1st solution
    # O(m + n) time | O(1) space
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        isEven = (m + n) % 2 == 0
        if isEven:
            mid = (m + n) // 2
        else:
            mid = (m + n) // 2 + 1 
            
        i, j = 0, 0

        for k in range(mid):
            v1 = nums1[i] if i < m else float('inf')
            v2 = nums2[j] if j < n else float('inf')
            curVal = min(v1, v2)
            print(curVal)
            if v1 <= v2:
                i += 1
            else:
                j += 1
        if isEven:
            v1 = nums1[i] if i < m else float('inf')
            v2 = nums2[j] if j < n else float('inf')
            curVal += min(v1, v2)
            return curVal / 2
        return curVal

                
