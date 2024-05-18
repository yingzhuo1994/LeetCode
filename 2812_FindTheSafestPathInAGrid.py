# 1st solution
# O(n^2 * log(n)) time | O(n^2) space
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distGrid = [[float("inf") for _ in range(n)] for _ in range(n)]
        thiefs = [[i, j] for i in range(n) for j in range(n) if grid[i][j] == 1]
        level = deque([[i, j, 0] for i, j in thiefs])
        while level:
            a, b, dist = level.popleft()
            if dist < distGrid[a][b]:
                distGrid[a][b] = dist
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    x = a + dx
                    y = b + dy
                    if 0 <= x < n and 0 <= y < n:
                        level.append([x, y, dist + 1])
        if distGrid[0][0] == 0 or distGrid[-1][-1] == 0:
            return 0
        
        def isValid(minDist):
            if distGrid[0][0] < minDist:
                return False
            level = deque([[0, 0]])
            visited = set([(0, 0)])
            while level:
                a, b = level.popleft()
                if (a, b) == (n-1, n-1):
                    return True
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    x = a + dx
                    y = b + dy
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited and distGrid[x][y] >= minDist:
                        visited.add((x, y))
                        level.append([x, y])
            return False
        start = 0
        end = n + n
        ans = 0
        while start < end:
            mid = start + (end - start) // 2
            if isValid(mid):
                start = mid + 1
                ans = max(ans, mid)
            else:
                end = mid
        return ans


# 2nd solution
# O(n^2 * log(n)) time | O(n^2) space
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        dis = [[-1] * n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
                    dis[i][j] = 0

        groups = [q]
        while q:  # 多源 BFS
            tmp = q
            q = []
            for i, j in tmp:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] < 0:
                        q.append((x, y))
                        dis[x][y] = len(groups)
            groups.append(q)  # 相同 dis 分组记录

        # 并查集模板
        fa = list(range(n * n))
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        
        # groups的最后一个q为空
        for d in range(len(groups) - 2, 0, -1):
            for i, j in groups[d]:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= dis[i][j]:
                        fa[find(x * n + y)] = find(i * n + j)
            if find(0) == find(n * n - 1):  # 写这里判断更快些
                return d
        return 0