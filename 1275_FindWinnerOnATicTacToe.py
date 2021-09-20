class Solution:
    # 1st solution
    # O(1) time | O(1) space
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0 for j in range(3)] for i in range(3)]
        for i, movie in enumerate(moves):
            x, y = movie
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