# 1st solution
# O(n^2) time | O(n) space 
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min2 = min(nums2)
        arr2 = [num - min2 for num in nums2]
        cnt2 = Counter(arr2)
        n = len(nums1)
        ans = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                arr1 = nums1[:i] + nums1[i+1:j] + nums1[j+1:]
                min1 = min(arr1)
                cnt1 = Counter(arr1)
                if len(cnt1) != len(cnt2):
                    continue
                if all(cnt1[num] == cnt2[num-min1] for num in cnt1):
                    ans = min(ans, min2 - min1)
        return ans



