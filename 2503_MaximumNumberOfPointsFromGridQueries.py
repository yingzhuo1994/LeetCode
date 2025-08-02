# 1st solution
# O(mn * log(mn) + k * log(mn)) time | O(mn + k) space
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        targets = []
        scores = []
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        target = grid[0][0] + 1
        score = 0
        while len(visited) < m * n:
            while minHeap and minHeap[0][0] < target:
                _, i, j = heappop(minHeap)
                if (i, j) not in visited:
                    score += 1
                    visited.add((i, j))
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                            heappush(minHeap, [grid[x][y], x, y])
            targets.append(target)
            scores.append(score)
            if minHeap:
                target = minHeap[0][0] + 1
        ans = []
        for query in queries:
            idx = bisect.bisect_right(targets, query) - 1
            if idx >= 0:
                ans.append(scores[idx])
            else:
                ans.append(0)
        return ans


# 2nd solution
# O(mn * log(mn) + k * log(k)) time | O(mn + k) space
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * len(queries)
        h = [(grid[0][0], 0, 0)]
        grid[0][0] = 0  # 充当 vis 数组的作用
        cnt = 0
        # 查询的下标按照查询值从小到大排序，方便离线
        for qi, q in sorted(enumerate(queries), key=lambda p: p[1]):
            while h and h[0][0] < q:
                cnt += 1
                _, i, j = heappop(h)
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):  # 枚举周围四个格子
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        heappush(h, (grid[x][y], x, y))
                        grid[x][y] = 0  # 充当 vis 数组的作用
            ans[qi] = cnt
        return ans