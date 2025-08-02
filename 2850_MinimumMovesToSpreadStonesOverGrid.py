# 1st solution
# O(1) time | O(1) space
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        source = []
        target = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1:
                    source.extend([(i, j) for _ in range(grid[i][j] - 1)])
                elif grid[i][j] == 0:
                    target.append((i, j))

        n = len(source)
        def dfs(idx, mask):
            if idx == n:
                return 0
            minDist = float("inf")
            for i in range(n):
                if mask & (1 << i):
                    continue
                dist = abs(source[idx][0] - target[i][0]) + abs(source[idx][1] - target[i][1])
                minDist = min(minDist, dist + dfs(idx + 1, mask | (1 << i)))
            return minDist
        return dfs(0, 0)
        