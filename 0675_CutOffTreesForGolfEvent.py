# 1st solution, BFS
# O((mn)^2) time | O((mn)^2) space
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        def query(x1, y1, x2, y2):
            if (x1, y1) == (x2, y2):
                return 0
            
            stack = [[x1, y1]]
            visited = set([(x1, y1)])
            dist = 1
            while stack:
                newStack = []
                for a, b in stack:
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        x = a + dx
                        y = b + dy
                        if 0 <= x < m and 0 <= y < n and forest[x][y] >= 1 and (x, y) not in visited:
                            if (x, y) == (x2, y2):
                                return dist
                            newStack.append([x, y])
                            visited.add((x, y))
                dist += 1
                stack = newStack
            
            return float("inf")
        
        cost = 0
        lst = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    lst.append([forest[i][j], i, j])
        lst.sort()
        last = [0, 0]
        for _, i, j in lst:
            dist = query(last[0], last[1], i, j)
            if dist == float("inf"):
                return -1
            cost += dist
            last = [i, j]
        
        return cost

# 2nd solution, A star
# O((mn)^2) time | O((mn)^2) space
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def astar(forest, sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            heap = [(0, 0, sr, sc)]
            cost = {(sr, sc): 0}
            while heap:
                f, g, r, c = heapq.heappop(heap)
                if r == tr and c == tc: 
                    return g
                for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                        if ncost < cost.get((nr, nc), 9999):
                            cost[nr, nc] = ncost
                            heapq.heappush(heap, (ncost, g+1, nr, nc))
            return -1
        
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = astar(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans