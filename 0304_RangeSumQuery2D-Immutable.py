class NumMatrix:
    # O(mn) time | O(mn) space
    def __init__(self, matrix: List[List[int]]):
        self.row, self.col = len(matrix), len(matrix[0])
        self.sumMatrix = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if i > 0 and j > 0:
                    left_top = self.sumMatrix[i-1][j-1]
                else:
                    left_top = 0
                
                if i > 0:
                    top = self.sumMatrix[i-1][j]
                else:
                    top = 0
                
                if j > 0:
                    left = self.sumMatrix[i][j-1]
                else:
                    left = 0
                
                self.sumMatrix[i][j] = left + top - left_top + matrix[i][j]

    # O(1) time | O(1) space
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            left_top = self.sumMatrix[row1 - 1][col1-1]
        else:
            left_top = 0
        
        if row1 > 0:
            top = self.sumMatrix[row1-1][col2]
        else:
            top = 0
        
        if col1 > 0:
            left = self.sumMatrix[row2][col1-1]
        else:
            left = 0
        
        return self.sumMatrix[row2][col2] - left - top + left_top
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)