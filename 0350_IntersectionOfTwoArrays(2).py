class Solution:
    # 1st solution
    # O(nlogn) time | O(n) space
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        lst = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                lst.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return lst

    # 2nd solution
    # O(n) time | O(n) space
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        lst = []
        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                lst.append(num)
                dic[num] -= 1
        return lst

    # 3rd solution
    # O(m + n) time | O(min(m, n)) space
    # where m, n are the length of nums1 and nums2, separately.
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        lst = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                lst.append(num)
                dic[num] -= 1
        return lst
