# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = 0
        countO = 0
        for row in board:
            for ch in row:
                if ch == "X":
                    countX += 1
                elif ch == "O":
                    countO += 1

        def checkWinner(player):
            for row in board:
                if all(ch == player for ch in row):
                    return True
            for j in range(3):
                if all(row[j] == player for row in board):
                    return True
            k = len(board)
            return all(board[i][i] == player for i in range(k)) or all(board[i][k-1-i] == player for i in range(k))
        if countX < countO or countX - countO > 1:
            return False
        if checkWinner("X"):
            if checkWinner("O"):
                return False
            elif countO == countX:
                return False
        elif checkWinner("O"):
            if countX != countO:
                return False
        return True

