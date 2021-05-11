class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def lookNeighbor(board, word, i, j, lst = []):
            if not word:
                return True
            top = (i - 1, j)
            bottom = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)
            result = False
            if 0 <= top[0] < len(board) and top not in lst and board[top[0]][top[1]] == word[0]:
                result = lookNeighbor(board, word[1:], top[0], top[1], lst + [top])
            if not result and 0 <= bottom[0] < len(board) and bottom not in lst and board[bottom[0]][bottom[1]] == word[0]:
                result = lookNeighbor(board, word[1:], bottom[0], bottom[1], lst + [bottom])
            if not result and 0 <= left[1] < len(board[0]) and left not in lst and board[left[0]][left[1]] == word[0]:
                result = lookNeighbor(board, word[1:], left[0], left[1], lst + [left])
            if not result and 0 <= right[1] < len(board[0]) and right not in lst and board[right[0]][right[1]] == word[0]:
                result = lookNeighbor(board, word[1:], right[0], right[1], lst + [right])
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    isContained = lookNeighbor(board, word[1:], i, j, [(i, j)])
                    if isContained:
                        return True
        return False
                    

    

