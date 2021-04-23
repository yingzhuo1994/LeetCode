class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1st solution
        # O(nlogn) time | O(n) space
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
        dic = {}
        lst = []
        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                lst.append(num)
                dic[num] -= 1
        return lst
