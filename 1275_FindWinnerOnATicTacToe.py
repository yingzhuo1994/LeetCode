class Solution:
    # 1st solution
    # O(1) time | O(1) space
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0 for j in range(3)] for i in range(3)]
        for i, move in enumerate(moves):
            x, y = move
            if i & 1 == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = -1

        return self.checkState(moves, grid)
    
    def checkState(self, moves, grid):
        for line in grid:
            count = sum(line)
            if self.getWinner(count) is not None:
                return self.getWinner(count)
        for j in range(3):
            count = 0
            for i in range(3):
                count += grid[i][j]
            if self.getWinner(count) is not None:
                return self.getWinner(count)
        count = 0
        for i in range(3):
            count += grid[i][i]
        if self.getWinner(count) is not None:
            return self.getWinner(count)
    
        count = 0
        for i in range(3):
            count += grid[2 - i][i]
        if self.getWinner(count) is not None:
            return self.getWinner(count)
            
        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"
    
    def getWinner(self, count):
        if count == 3:
            return "A"
        elif count == -3:
            return "B"
        else:
            return None

    # 2nd solution
    # O(m) time | O(n) space
    def tictactoe(self, moves: List[List[int]]) -> str:

        # n stands for the size of the board, n = 3 for the current game.
        n = 3

        # use rows and cols to record the value on each row and each column.
        # diag1 and diag2 to record value on diagonal or anti-diagonal.
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        # Two players having value of 1 and -1, player_1 with value = 1 places first.
        player = 1
        
        for row, col in moves:
            
            # Update the row value and column value.
            rows[row] += player
            cols[col] += player
            
            # If this move is placed on diagonal or anti-diagonal, 
            # we shall update the relative value as well.
            if row == col:            
                diag += player
            if row + col == n - 1:
                anti_diag += player
                
            # check if this move meets any of the winning conditions.
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player == 1 else "B"
        
            # If no one wins so far, change to the other player alternatively. 
            # That is from 1 to -1, from -1 to 1.
            player *= -1
            
        # If all moves are completed and there is still no result, we shall check if 
        # the grid is full or not. If so, the game ends with draw, otherwise pending.
        return "Draw" if len(moves) == n * n else "Pending"   
        