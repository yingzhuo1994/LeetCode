class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def lookNeighbor(board, word, i, j, lst = []):
            if not word:
                return True
            result = False
            if 0 <= i - 1 < len(board) and (i - 1, j) not in lst and board[i - 1][j] == word[0]:
                result = lookNeighbor(board, word[1:], i - 1, j, lst + [(i - 1, j)])
            if not result and 0 <= i + 1 < len(board) and (i + 1, j) not in lst and board[i + 1][j] == word[0]:
                result = lookNeighbor(board, word[1:], i + 1, j, lst + [(i + 1, j)])
            if not result and 0 <= j - 1 < len(board[0]) and (i, j - 1) not in lst and board[i][j - 1] == word[0]:
                result = lookNeighbor(board, word[1:], i, j - 1, lst + [(i, j - 1)])
            if not result and 0 <= j + 1 < len(board[0]) and (i, j + 1) not in lst and board[i][j + 1] == word[0]:
                result = lookNeighbor(board, word[1:], i, j + 1, lst + [(i, j + 1)])
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    isContained = lookNeighbor(board, word[1:], i, j, [(i, j)])
                    if isContained:
                        return True
        return False
                    

    

