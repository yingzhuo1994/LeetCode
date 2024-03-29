# 1st solution, BFS
# O(n^2) time | O(n^2) space
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0:
            return -1
        if grid[-1][-1] != 0:
            return -1
        level = set([(0, 0)])
        grid[0][0] = 1
        step = 1
        while level:
            nextLevel = set()
            for i, j in level:
                if (i, j) == (n - 1, n - 1):
                    return step
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and (x, y) != (i, j) and grid[x][y] == 0:
                            nextLevel.add((x, y))
                            grid[x][y] = 1
            step += 1
            level = nextLevel
        return -1

# 2nd solution, Two Direction BFS
# O(n^2) time | O(n^2) space
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0:
            return -1
        if grid[-1][-1] != 0:
            return -1
        small = set([(0, 0)])
        large = set([(n - 1, n - 1)])
        step = 1
        visited = set()
        while small:
            nextLevel = set()
            if len(small) > len(large):
                small, large = large, small
            for i, j in small:
                visited.add((i, j))
                if (i, j) in large:
                    return step
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                            nextLevel.add((x, y))
            step += 1
            small = nextLevel
        return -1