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

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        cnt = Counter(tuple(row) for row in grid)
        for tpl in zip(*grid):
            pairs += cnt[tpl]
        return pairs