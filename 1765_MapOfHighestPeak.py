# 1st solution
# O(mn) time | O(1) space
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        level = deque([[i, j, 0] for i in range(m) for j in range(n) if isWater[i][j] == 1])
        heights = [[0 for _ in range(n)] for _ in range(m)]
        while level:
            i, j, h = level.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and isWater[x][y] == 0 and heights[x][y] == 0:
                    heights[x][y] = h + 1
                    level.append([x, y, h + 1])
        return heights