# 1st solution
# O(mn) time | O(1) space
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n =len(matrix), len(matrix[0])
        neg = 0
        minVal = float("inf")
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0:
                    neg += 1
                minVal = min(minVal, abs(matrix[i][j]))
                ans += abs(matrix[i][j])
        if neg & 1:
            ans -= 2 * minVal
        return ans
