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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last = {c: i for i, pgm in enumerate(garbage) for c in pgm}
        dis = list(accumulate(travel, initial = 0))
        return sum(map(len, garbage)) + sum(dis[last.get(c, 0)] for c in 'PGM')

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last = {c: i for i, pgm in enumerate(garbage) for c in pgm}
        ans = sum(map(len, garbage))
        idxOrder = sorted(last.values())
        idx = 0
        i = 0
        dist = 0
        while idx < len(idxOrder):
            while i < idxOrder[idx]:
                if i < len(travel):
                    dist += travel[i]
                i += 1
            ans += dist
            idx += 1
        return  ans