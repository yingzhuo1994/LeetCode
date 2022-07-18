# 1st solution, TLE
# O(m^2 * n^2) time | O(m^2 * n^2) space
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        ans = 0
        for dx in range(m):
            for dy in range(n):
                for x1 in range(m):
                    x2 = x1 + dx
                    if x2 >= m:
                        break 
                    for y1 in range(n):
                        y2 = y1 + dy
                        if y2 >= n:
                            break
                        if dx == 0 and dy == 0:
                            sumValue = matrix[x1][y1]
                        else:
                            sumValue = memo.get((x1, y1, x2 - 1, y2), 0) + memo.get((x1, y1, x2, y2 - 1), 0) - memo.get((x1, y1, x2 - 1, y2 - 1), 0) + matrix[x2][y2]
                        memo[(x1, y1, x2, y2)] = sumValue
                        if sumValue == target:
                            ans += 1
        return ans

# 2nd solution, TLE
# O(m*n^2) time | O(m) space
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            for j in range(n - 1):
                row[j + 1] += row[j]
        ans = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                count = collections.defaultdict(int)
                curTotal, count[0] = 0, 1
                for x in range(m):
                    curTotal += matrix[x][y2] - (matrix[x][y1 - 1] if y1 > 0 else 0)
                    ans += count[curTotal - target]
                    count[curTotal] += 1
        return ans