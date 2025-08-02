# 1st solution
# O(nmn * log(mn)) time | O(mn) space
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dp = [[inf] * m for i in range(n)]
        h = [[0, 0, 0]] # arrive time, i, j
        moveTime[0][0] = -1
        while h:
            t, i, j = heappop(h)
            if t >= dp[i][j]: continue
            if i == n - 1 and j == m - 1: return t
            dp[i][j] = t
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x, y = i + di, j + dj
                c = (i + j) % 2 + 1
                if 0 <= x < n and 0 <= y < m and dp[x][y] == inf:
                    heappush(h, [max(moveTime[x][y], t) + c, x, y])