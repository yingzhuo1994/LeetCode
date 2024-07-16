# 1st solution
# O(n + m) time | O(n + m) space
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans1 = 0
        ans2 = 0
        for key in cnt1:
            if key in cnt2:
                ans1 += cnt1[key]
        
        for key in cnt2:
            if key in cnt1:
                ans2 += cnt2[key]
        
        return [ans1, ans2]