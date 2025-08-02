# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        answer = [row[:] for row in matrix]
        for j in range(n):
            val = max([matrix[i][j] for i in range(m)])
            for i in range(m):
                if answer[i][j] == -1:
                    answer[i][j] = val
        return answer