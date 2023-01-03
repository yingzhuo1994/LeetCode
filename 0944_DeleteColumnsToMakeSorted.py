# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        mat = [list(s) for s in strs]
        m, n = len(mat), len(mat[0])
        deletedCols = []
        for j in range(n):
            last = "a"
            for i in range(m):
                if mat[i][j] < last:
                    deletedCols.append(j)
                    break
                last = mat[i][j]
        
        # def merge(lst):
        #     stack = []
        #     for i in range(len(lst)):
        #         if i in deletedCols:
        #             continue
        #         else:
        #             stack.append(lst[i])
        #     return "".join(stack)
        
        return len(deletedCols)