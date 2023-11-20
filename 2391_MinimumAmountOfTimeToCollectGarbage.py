# 1st solution
# O(n) time | O(1) space
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def collectGarbage(target):
            ans = 0
            curDist = 0
            for i in range(len(garbage)):
                v = garbage[i].count(target)
                if v > 0:
                    ans += curDist + v
                    curDist = 0
                if i < len(travel):
                    curDist += travel[i]
            return ans
        ans = 0
        for ch in "MPG":
            ans += collectGarbage(ch)
        return ans