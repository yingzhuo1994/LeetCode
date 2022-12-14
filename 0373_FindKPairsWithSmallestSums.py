# 1st solution, TLE
# O(mnlog(mn)) time | O(mn) space
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        dic = defaultdict(list)
        for a in nums1:
            for b in nums2:
                dic[a + b].append([a, b])
        keys = sorted(dic.keys())
        for key in keys:
            if len(ans) + len(dic[key]) <= k:
                ans.extend(dic[key])
            else:
                ans.extend(dic[key][:k - len(ans)])
                break
        return ans

# 2nd solution
# O(m * log(n)) time | O(k) space
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        
        def countTarget(target):
            count = 0
            for i in range(m):
                idx = bisect.bisect_right(nums2, target - nums1[i])
                count += idx
                if idx == 0:
                    break
            return count
        
        left = nums1[0] + nums2[0]
        right = nums1[-1] + nums2[-1]
        while left < right:
            mid = left + (right - left) // 2
            if countTarget(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        ans = []
        for i in range(m):
            idx = bisect.bisect_left(nums2, right - nums1[i])
            if idx + len(ans) <= k:
                for j in range(idx):
                    ans.append([nums1[i], nums2[j]])
            else:
                for j in range(k - len(ans)):
                    ans.append([nums1[i], nums2[j]])
                break
        for i in range(m):
            if len(ans) == k:
                break
            idx = bisect.bisect_left(nums2, right - nums1[i])
            for j in range(idx, n):
                if nums1[i] + nums2[j] == right and len(ans) < k:
                    ans.append([nums1[i], nums2[j]])
        return ans