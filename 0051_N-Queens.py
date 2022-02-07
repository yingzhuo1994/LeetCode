# 1st solution
# O(n!) time | O(n) space
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        blockedColumns = set()
        blockedDownDiagonals = set()
        blockedUpDiagonals = set()
        ans = []
        self.getSolutions(0, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, n, ans, [])
        return ans

    def getSolutions(self, row, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize, ans, lst):
        if row == boardSize:
            ans.append(lst)
            return
        for col in range(boardSize):
            if self.isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
                self.placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
                cur = ""
                for k in range(boardSize):
                    if k == col:
                        cur += "Q"
                    else:
                        cur += "."
                self.getSolutions(row + 1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize, ans, lst + [cur])
                self.removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)

    def isNonAttackingPlacement(self, row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
        if col in blockedColumns:
            return False
        if row + col in blockedUpDiagonals:
            return False
        if row - col in blockedDownDiagonals:
            return False
        return True

    def placeQueen(self, row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
        blockedColumns.add(col)
        blockedUpDiagonals.add(row + col)
        blockedDownDiagonals.add(row - col)

    def removeQueen(self, row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
        blockedColumns.remove(col)
        blockedUpDiagonals.remove(row + col)
        blockedDownDiagonals.remove(row - col)