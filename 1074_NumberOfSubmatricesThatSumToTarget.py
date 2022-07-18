# 1st solution, TLE
# O(m^2 * n^2) time | O(m^2 * n^2) space
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = {(1, 1): matrix}
        for j in range(2, n + 1):
            lastMatrix = memo[(1, j - 1)]
            newMatrix = [[0 for _ in range(n - j + 1)] for _ in range(m)]
            for x in range(m):
                for y in range(n - j + 1):
                    newMatrix[x][y] = lastMatrix[x][y] + matrix[x][j + y - 1]

            memo[(1, j)] = newMatrix
        
        for i in range(2, m + 1):
            for j in range(1, n + 1):
                firstMatrix = memo[(1, j)]
                lastMatrix = memo[(i - 1, j)]
                newMatrix = [[0 for _ in range(n - j + 1)] for _ in range(m - i + 1)]
                for x in range(m - i + 1):
                    for y in range(n - j + 1):
                        newMatrix[x][y] = lastMatrix[x][y] + firstMatrix[i + x -1][y]

                memo[(i, j)] = newMatrix
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ans += self.checkMatrix(memo[(i, j)], target)
        
        return ans

    def checkMatrix(self, matrix, target):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    count += 1
        return count