class Solution:
    # 1st solution
    # O(mn) time | O(1) space
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowEnd = len(board) - 1
        colEnd = len(board[0]) - 1 
        for i in range(len(board)):
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            if board[i][colEnd] == "O":
                self.dfs(board, i, colEnd)
        
        for j in range(1, colEnd):
            if board[0][j] == "O":
                self.dfs(board, 0, j)
            if board[rowEnd][j] == "O":
                self.dfs(board, rowEnd, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board
    
    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "O":
            board[i][j] = "T"
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                row, col = i + x, j + y
                self.dfs(board, row, col)

    # 2nd solution
    def solve(self, board: List[List[str]]) -> None:
        if not any(board): return

        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        for row in board:
            for i, c in enumerate(row):
                row[i] = 'O' if c == 'S' else 'X'
        
        