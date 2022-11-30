# 1st solution
# O(mn) time | O(k) space
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def isBattleship(i, j):
            if board[i][j] != "X":
                return False
            board[i][j] = "."
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    isBattleship(x, y)
            return True
        
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if isBattleship(i, j):
                    count += 1
        return count

# 2nd solution
# O(mn) time | O(1) space
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count