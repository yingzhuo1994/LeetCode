# 1st solution
# O(n) time | O(1) space
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]

        ans = 0
        for i in range(n):
            ans += mat[i][i]
        for i in range(n):
            j = n - 1 - i
            ans += mat[i][j]
        
        if n & 1:
            i = n // 2
            ans -= mat[i][i]
        
        return ans
