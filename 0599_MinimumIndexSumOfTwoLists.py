# 1st solution
# O(m + n) time | O(m) space
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        for i, s in enumerate(list1):
            dic[s] = i
        
        ans = [float('inf')]
        for i, s in enumerate(list2):
            if s in dic:
                idx = dic[s] + i
                if idx < ans[0]:
                    ans = [idx, s]
                elif idx == ans[0]:
                    ans.append(s)
    
        return ans[1:]