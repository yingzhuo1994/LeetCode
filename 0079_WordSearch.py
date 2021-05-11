class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def lookNeighbor(board, word, i, j, lst = []):
            if not word:
                return []
            top = (i - 1, j)
            bottom = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)
            possible = []
            if 0 <= top[0] < len(board) and top not in lst and board[top[0]][top[1]] == word[0]:
                possible.append(top)
            if 0 <= bottom[0] < len(board) and bottom not in lst and board[bottom[0]][bottom[1]] == word[0]:
                possible.append(bottom)
            if 0 <= left[0] < len(board[0]) and left not in lst and board[left[0]][left[1]] == word[0]:
                possible.append(left)
            if 0 <= right[0] < len(board[0]) and right not in lst and board[right[0]][right[1]] == word[0]:
                possible.append(right)
            return possible

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    lst = []
                    nextPlaceLst = lookNeighbor(board, word[1:], i, j, lst)
                    

    

