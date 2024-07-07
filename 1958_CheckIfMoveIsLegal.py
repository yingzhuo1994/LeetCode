# 1st solution
# O(1) time | O(1) space
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for dx, dy in dirs:
            count = 0
            i, j = rMove + dx, cMove + dy
            isValid = False
            while 0 <= i < m and 0 <= j < n:
                if board[i][j] == ".":
                    break
                elif board[i][j] == color:
                    isValid = count >= 1
                    break
                else:
                    count += 1
                i += dx
                j += dy
            if isValid:
                return True
        return False