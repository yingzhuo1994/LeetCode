# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        topLeft = [[0 for _ in range(n)] for _ in range(m)]
        bottomRight = [[0 for _ in range(n)] for _ in range(m)]
        ans = [[0 for _ in range(n)] for _ in range(m)]

        for d in range(-n, m):
            values = set()
            for i in reversed(range(m)):
                j = i - d
                if 0 <= j < n:
                    topLeft[i][j] = len(values)
                    values.add(grid[i][j])

        for d in range(-n, m):
            values = set()
            for i in range(m):
                j = i - d
                if 0 <= j < n:
                    bottomRight[i][j] = len(values)  
                    values.add(grid[i][j])
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = abs(topLeft[i][j] - bottomRight[i][j])
        
        return ans
