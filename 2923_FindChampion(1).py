# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        records = [True for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if grid[i][j]:
                    records[j] = False
                else:
                    records[i] = False
        for i in range(n):
            if records[i]:
                return i