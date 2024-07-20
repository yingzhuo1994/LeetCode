# 1st solution
# O((m + n)^2) time | O(m * n) space
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        def findMin(array, visited):
            val = float("inf")
            idx = -1
            for i, num in enumerate(array):
                if visited[i]:
                    continue
                if num < val:
                    val = num
                    idx = i
            return idx, val
        
        rowVisited = [False for _ in range(m)]
        colVisited = [False for _ in range(n)]
        for _ in range(m + n - 1):
            i, minRow = findMin(rowSum, rowVisited)
            j, minCol = findMin(colSum, colVisited)

            if minRow <= minCol:
                rowVisited[i] = True
                for k in range(n):
                    if not colVisited[k]:
                        matrix[i][k] = minRow
                        colSum[k] -= minRow
                        break
            else:
                colVisited[j] = True 
                for k in range(m):
                    if not rowVisited[k]:
                        matrix[k][j] = minCol
                        rowSum[k] -= minCol
                        break

        return matrix
        
        