class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def checkConnection(board, lst, i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "O":
                if [i, j] not in lst:
                    lst.append([i, j])
                    checkConnection(board, lst, i + 1, j)
                    checkConnection(board, lst, i - 1, j)
                    checkConnection(board, lst, i, j + 1)
                    checkConnection(board, lst, i, j - 1)


        nearBorder = []
        rowEnd = len(board) - 1
        colEnd = len(board[0]) - 1
        for i in range(len(board)):
            if board[i][0] == "O":
                nearBorder.append([i, 0])
            if board[i][colEnd] == "O":
                nearBorder.append([i, colEnd])
        for j in range(1, colEnd):
            if board[0][j] == "O":
                nearBorder.append([0, j])
            if board[rowEnd][j] == "O":
                nearBorder.append([rowEnd, j])
        oLst = []
        for pair in nearBorder:
            checkConnection(board, oLst, pair[0], pair[1])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if [i, j] not in oLst:
                    board[i][j] = "X"

        # 2nd solution
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
        
        