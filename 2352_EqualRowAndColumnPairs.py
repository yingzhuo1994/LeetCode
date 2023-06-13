# 1st solution
# O(n^3) time | O(1) space
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                valid = all(grid[i][k] == grid[k][j] for k in range(n))
                if valid:
                    count += 1
        return count