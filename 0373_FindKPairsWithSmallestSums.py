# 1st solution, TLE
# O(nlog(n)) time | O(n^2) space
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