# 1st solution
# O(mn * log(mn)) time | O(mn) space
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