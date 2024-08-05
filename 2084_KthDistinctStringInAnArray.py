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

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}
        for i, s in enumerate(arr):
            if s not in dic:
                dic[s] = []
            if len(dic[s]) > 1:
                continue
            dic[s].append(i)
        distinct_strs = [[dic[s][0], s] for s in dic if len(dic[s]) == 1]
        if len(distinct_strs) < k:
            return ""
        distinct_strs.sort()
        return distinct_strs[k-1][1]