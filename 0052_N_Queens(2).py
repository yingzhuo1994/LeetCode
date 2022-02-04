# 1st solution
# O(n!) time | O(n) space
class Solution:
    def totalNQueens(self, n: int) -> int:
        blockedColumns = set()
        blockedUpDiagonals = set()
        blockedDownDiagonals = set()
        return self.getNumberOfNonAttackingQueenPlacements(0, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, n)

    def getNumberOfNonAttackingQueenPlacements(self, row, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize):
        if row == boardSize:
            return 1
        
        validPlacements = 0
        for col in range(boardSize):
            if self.isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
                self.placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
                validPlacements += self.getNumberOfNonAttackingQueenPlacements(
                    row + 1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize
                )
                self.removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
        
        return validPlacements
       
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