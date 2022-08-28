# 1st solution
# O((m + n) * D * log(D)) time | O(D) space
# where D = min(m + n)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def modifyMatrix(startRow, startCol):
            nums = []
            x, y = startRow, startCol
            while x < m and y < n:
                nums.append(mat[x][y])
                x += 1
                y += 1
            nums.sort()
            k = 0
            x, y = startRow, startCol
            while x < m and y < n:
                mat[x][y] = nums[k]
                x += 1
                y += 1
                k += 1

        m, n = len(mat), len(mat[0])
        for j in range(n):
            modifyMatrix(0, j)
        
        for i in range(1, m):
            modifyMatrix(i, 0)

        return mat