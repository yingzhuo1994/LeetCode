class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1st solution
        rowDic = {}
        columnDic = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowDic[i] = rowDic.get(i, 0) + 1
                    columnDic[j] = columnDic.get(j, 0) + 1

        for i in rowDic:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for j in columnDic:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        
