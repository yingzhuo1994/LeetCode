# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dic = {}
        for i in range(m):
            for j in range(n):
                dic[mat[i][j]] = (i, j)
        rowDic = {i: 0 for i in range(m)}
        colDic = {j: 0 for j in range(n)}
        for idx, val in enumerate(arr):
            i, j = dic[val]
            rowDic[i] += 1
            colDic[j] += 1
            if rowDic[i] == n or colDic[j] == m:
                return idx
        return -1