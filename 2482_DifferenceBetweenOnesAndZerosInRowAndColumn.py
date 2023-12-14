# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = {i: 0 for i in range(m)}
        cols = {j: 0 for j in range(n)}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                else:
                    rows[i] -= 1
                    cols[j] -= 1
        
        matrix = [[rows[i] + cols[j] for j in range(n)] for i in range(m)]
        return matrix