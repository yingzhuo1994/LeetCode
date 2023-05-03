# 1st solution
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans = [[], []]
        for num1 in set1:
            if num1 not in set2:
                ans[0].append(num1)
        
        for num2 in set2:
            if num2 not in set1:
                ans[1].append(num2)
        
        return ans