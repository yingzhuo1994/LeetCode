# O(9^k) time | O(k) space
# where k is the number of empty cells
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        emptyLst = []
        numsLst = [str(i) for i in range(1, 10)]
        rowTable = {}
        colTable = {}
        gridTable = {}
        for i in range(n):
            rowTable[i] = {}
            for num in numsLst:
                rowTable[i][num] = False

        for i in range(n):
            colTable[i] = {}
            for num in numsLst:
                colTable[i][num] = False

        for i in range(3):
            for j in range(3):
                gridTable[(i, j)] = {}
                for num in numsLst:
                    gridTable[(i, j)][num] = False        

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    emptyLst.append([i, j])
                else:
                    rowTable[i][num] = True
                    colTable[j][num] = True
                    gridTable[(i//3, j//3)][num] = True

        if len(emptyLst) > 0:
            self.dfs(board, emptyLst, rowTable, colTable, gridTable, 0)
    
    
    def dfs(self, board, emptyLst, rowTable, colTable, gridTable, idx):
        if idx == len(emptyLst):
            return True
        
        numsLst = [str(i) for i in range(1, 10)]
        x, y = emptyLst[idx]
        for num in numsLst:
            if rowTable[x][num] or colTable[y][num] or gridTable[(x//3, y//3)][num]:
                continue
            board[x][y] = num
            rowTable[x][num] = True
            colTable[y][num] = True
            gridTable[(x//3, y//3)][num] = True
            if self.dfs(board, emptyLst, rowTable, colTable, gridTable, idx + 1):
                return True
            board[x][y] = "."
            rowTable[x][num] = False
            colTable[y][num] = False
            gridTable[(x//3, y//3)][num] = False
        return False