# 1st solution
# O(kmn) time | O(mn) space
# where k = maxMove
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        if m == 1 and n == 1:
            return 4
        MOD = 10**9 + 7
        ans = 0

        moves = maxMove
        level = {(startRow, startColumn): 1}
        neibs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while moves > 0 and level:
            newLevel = {}
            for i, j in level:
                count = 0
                if i == 0:
                    count += 1
                if i == m - 1:
                    count += 1
                if j == 0:
                    count += 1
                if j == n - 1:
                    count += 1
                ans += level[(i, j)] * count
                ans %= MOD

                for dx, dy in neibs:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n:
                        newLevel[(x, y)] = newLevel.get((x, y), 0) + level[(i, j)]

            level = newLevel
            moves -= 1
        return ans