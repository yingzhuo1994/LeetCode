# 1st solution
# O(m + n) time | O(1) space
class Solution:
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

# 2nd solution
# O(log(m + n)) time | O(1) space
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        
        iMin, iMax, half_len = 0, m, (m + n + 1) // 2
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, we must increase it
                iMin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, we must decrease it
                iMax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                
                return (max_of_left + min_of_right) / 2

                


                
