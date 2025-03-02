# 1st solution
# O(m + n) time | O(m + n) space
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        array = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                if array and array[-1][0] == nums1[i][0]:
                    array[-1][1] += nums1[i][1]
                else:
                    array.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                if array and array[-1][0] == nums2[j][0]:
                    array[-1][1] += nums2[j][1]
                else:
                    array.append(nums2[j])
                j += 1
            else:
                id = nums1[i][0]
                val = nums1[i][1] + nums2[j][1]
                array.append([id, val])
                i += 1
                j += 1
        if i < len(nums1):
            if array and array[-1][0] == nums1[i][0]:
                array[-1][1] += nums1[i][1]
                i += 1
            array.extend(nums1[i:])
        if j < len(nums2):
            if array and array[-1][0] == nums2[j][0]:
                array[-1][1] += nums2[j][1]
                j += 1
            array.extend(nums2[j:])
        return array            