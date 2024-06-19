# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        flowers = [[day, idx] for idx, day in enumerate(bloomDay)]
        flowers.sort()
        DS = DisjointSet(n)
        bloomSet = set()
        count = 0
        for day, idx in flowers:
            bloomSet.add(idx)
            if k == 1:
                count += 1
            for neig in [idx - 1, idx + 1]:
                if neig in bloomSet:
                    size1 = DS.getSize(idx)
                    size2 = DS.getSize(neig)
                    if DS.merge(idx, neig):
                        _, r1 = divmod(size1, k)
                        _, r2 = divmod(size2, k)
                        r = r1 + r2
                        count += r // k
            if count >= m:
                return day
        return -1

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def getParent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        px, py = self.getParent(x), self.getParent(y)
        if px == py:
            return False
        if self.size[px] < self.size[py]:
            x, y = y, x
            px, py = py, px
        self.size[px] += self.size[py]
        self.parents[py] = px
        return True
    
    def getSize(self, x):
        px = self.getParent(x)
        return self.size[px]


# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def enough(target):
            count = 0
            flowers = 0
            for day in bloomDay:
                if day <= target:
                    flowers += 1
                else:
                    count += flowers // k
                    flowers = 0
            count += flowers // k
            return count >= m
        start = 1
        end = max(bloomDay)
        ans = float("inf")
        while start <= end:
            mid = start + (end - start) // 2
            if enough(mid):
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
        if ans == float("inf"):
            return -1
        return ans