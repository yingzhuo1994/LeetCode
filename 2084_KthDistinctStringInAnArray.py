# 1st solution
# O(n) time | O(n) space
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = collections.Counter(arr)
        distinct_strs = set([s for s in cnt if cnt[s] == 1])
        if len(distinct_strs) < k:
            return ""
        order = 0
        for s in arr:
            if s in distinct_strs:
                order += 1
            if order == k:
                return s