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

# 2nd simplified solution
# O(m*n*4^l) time | O(m * n + l) space
# where m and n are the row number and column number of board, and l is the length of word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def lookNeighbor(board, word, i, j, k, lst = []):
            if k > len(word) - 1:
                return True
            result = False
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in lst and board[i][j] == word[k]:
                result = lookNeighbor(board, word, i - 1, j, k + 1, lst + [(i, j)]) \
                      or lookNeighbor(board, word, i + 1, j, k + 1, lst + [(i, j)]) \
                      or lookNeighbor(board, word, i, j - 1, k + 1, lst + [(i, j)]) \
                      or lookNeighbor(board, word, i, j + 1, k + 1, lst + [(i, j)])
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                isContained = lookNeighbor(board, word, i, j, 0, [])
                if isContained:
                    return True
        return False
    
# 3rd solution
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False
    
    def dfs(self, board, i, j, word, k):
        if board[i][j] == word[k] and k == len(word) - 1:
            return True
        if board[i][j] != word[k]:
            return False
        temp = board[i][j]
        board[i][j] = "#"
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            row, col = i + x, j + y
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if self.dfs(board, row, col, word, k + 1):
                    return True
        board[i][j] = temp
        return False

