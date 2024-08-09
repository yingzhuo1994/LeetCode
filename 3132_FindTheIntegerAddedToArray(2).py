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


# 2nd solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        cnt2 = Counter(nums2)
        min2 = min(cnt2.keys())
        ans = float("inf")
        for idx in range(3):
            if idx > 0 and nums1[idx] == nums1[idx - 1]:
                continue
            min1 = nums1[idx]
            cnt1 = Counter([nums1[i] - min1 for i in range(idx, len(nums1))])
            if all(cnt1[num-min2] >= cnt2[num] for num in cnt2):
                ans = min(ans, min2 - min1)
        return ans