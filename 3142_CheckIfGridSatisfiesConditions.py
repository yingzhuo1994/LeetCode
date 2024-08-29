# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        columns = list(zip(*grid))
        for column in columns:
            if len(set(column)) != 1:
                return False
        for j in range(len(grid[0]) - 1):
            if grid[0][j] == grid[0][j + 1]:
                return False
        return True

# 2nd solution
# O(mn) time | O(1) space
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for j in range(len(grid[0]) - 1):
            if grid[0][j] == grid[0][j + 1]:
                return False

        for j in range(n):
            val = grid[0][j]
            for i in range(1, m):
                if grid[i][j] != val:
                    return False
        return True