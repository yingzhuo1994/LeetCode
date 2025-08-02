# 1st solution
# O(mn) time | O(1) space 
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(rStart, cStart):
            if not all(sum([grid[i][j] for i in range(rStart, rStart + 3)]) == 15 for j in range(cStart, cStart + 3)):
                return False
            if not all(sum([grid[i][j] for j in range(cStart, cStart + 3)]) == 15 for i in range(rStart, rStart + 3)):
                return False
            if not sum(grid[i][j] for i, j in zip(range(rStart, rStart + 3), range(cStart, cStart + 3))) == 15:
                return False
            if not sum(grid[i][j] for i, j in zip(reversed(range(rStart, rStart + 3)), range(cStart, cStart + 3))) == 15:
                return False
            valid = {i: False for i in range(1, 10)}
            for i in range(rStart, rStart + 3):
                for j in range(cStart, cStart + 3):
                    if 1 <= grid[i][j] <= 9:
                        valid[grid[i][j]] = True
                    else:
                        return False
            return all(valid.values())
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                ans += check(i, j)
        return ans