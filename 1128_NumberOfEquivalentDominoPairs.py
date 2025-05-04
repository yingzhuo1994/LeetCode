# 1st solution
# O(n) time | O(1) space
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = {}
        ans = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            if key in dic:
                ans += dic[key]
            dic[key] = dic.get(key, 0) + 1
        return ans