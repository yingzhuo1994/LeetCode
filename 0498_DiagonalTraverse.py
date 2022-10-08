# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        i, j = 0, 0
        m, n = len(mat), len(mat[0])
        dx, dy = -1, 1
        count = 0
        while count < m * n:
            ans.append(mat[i][j])
            i += dx
            j += dy
            if i < 0 or j >= n:
                if i < 0 and j >= n:
                    i = 1
                    j = n - 1
                elif i < 0:
                    i += 1
                else:
                    i += 2
                    j = n - 1
                dx = -dx
                dy = -dy
            elif i >= m or j < 0:
                if i >= m and j < 0:
                    i = m - 1
                    j = 1
                elif j < 0:
                    j = 0
                else:
                    i = m - 1
                    j += 2
                dx = -dx
                dy = - dy
            count += 1
        return ans