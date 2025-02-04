# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array1 = sorted(nums1)
        array2 = sorted([num, idx] for idx, num in enumerate(nums2))
        ans = [-1 for _ in range(len(nums1))]
        i = 0
        left = []
        for j in range(len(array2)):
            num2, idx = array2[j]
            while i < len(nums1) and array1[i] <= num2:
                left.append(i)
                i += 1
            if i >= len(nums1):
                break

            ans[idx] = array1[i]
            i += 1
        i = 0
        for j in left:
            while ans[i] >= 0:
                i += 1
            ans[i] = array1[j]
            i += 1
        return ans
