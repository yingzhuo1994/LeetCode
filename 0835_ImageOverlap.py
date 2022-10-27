# 1st solution
# O(n^4) time | O(1) space
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        n = len(img1)
        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                overlap = self.translateCompare(img1, img2, dx, dy)
                ans = max(ans, overlap)
        return ans
    
    def translateCompare(self, img1, img2, dx, dy):
        n = len(img1)
        rowStart = max(-dx, 0)
        rowEnd =  min(n - 1, n  - 1 - dx)
        colStart = max(-dy, 0)
        colEnd = min(n - 1, n - 1 - dy)
        
        count = 0
        for i in range(rowStart, rowEnd + 1):
            for j in range(colStart, colEnd + 1):
                if img1[i][j] == img2[i+dx][j+dy] and img1[i][j] == 1:
                    count += 1
        return count

# 2nd solution
# O(n^4) time | O(1) space
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M in up-left and up-right directions 
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            left_shift_count, right_shift_count = 0, 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        left_shift_count += 1
                    if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
                        right_shift_count += 1

            return max(left_shift_count, right_shift_count)

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions 
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps