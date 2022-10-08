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

# 2nd solution
# O(mn) time | O(mn) space
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        # Variables to track the size of the mat
        N, M = len(mat), len(mat[0])
        
        # The two arrays as explained in the algorithm
        result, intermediate = [], []
        
        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(N + M - 1):
            
            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()
            
            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            
            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            # Reverse even numbered diagonals. The
            # article says we have to reverse odd 
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result    