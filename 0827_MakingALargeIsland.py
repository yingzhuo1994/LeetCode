# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def getIdx(i, j):
            return i * n + j
        DS = DisjointSet(n * n)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                a = getIdx(i, j)
                if i + 1 < n and grid[i + 1][j] == 1:
                    b = getIdx(i + 1, j)
                    DS.merge(a, b)
                if j + 1 < n and grid[i][j + 1] == 1:
                    b = getIdx(i, j + 1)
                    DS.merge(a, b)
        
        ans = max(DS.size)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    candidates = set()
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            b = getIdx(x, y)
                            candidates.add(DS.getParent(b))
                    cnt = sum([DS.getSize(p) for p in candidates]) + 1
                    ans = max(ans, cnt)

        ans = min(ans, n * n)
        return ans


class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def merge(self, a, b):
        pa, pb = self.getParent(a), self.getParent(b)
        if pa == pb:
            return False
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parents[pb] = pa
        self.size[pa] += self.size[pb]
        return True
    
    def getParent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]
    
    def getSize(self, x):
        p = self.getParent(x)
        return self.size[p]