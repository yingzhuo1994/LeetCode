# 1st solution
# O(n) time | O(n) space
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        ans = []
        for i, g in enumerate(groupSizes):
            if g not in dic:
                dic[g] = []

            dic[g].append(i)
            if len(dic[g]) == g:
                ans.append(dic[g])
                dic[g] = []
        
        return ans
            