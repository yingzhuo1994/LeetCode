# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = sum(sum(1 if val > 0 else 0 for val in row) for row in grid)
        xz = sum([max(row) for row in grid])
        yz = sum([max([grid[i][j] for i in range(n)]) for j in range(n)])
        return xy + xz + yz


# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        hor = sum(map(max, grid))
        ver = sum(map(max, zip(*grid)))
        top = sum(v > 0 for row in grid for v in row)
        return ver + hor + top