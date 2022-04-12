# O(mn) time | O(1) space
class Solution:
    # 0,2 are "dead", and "dead->live"
    # 1,3 are "live", and "live->dead"
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                liveCount = self.countNeighborsLives(board, i, j)
                if board[i][j] == 0 or board[i][j] == 2:
                    if liveCount == 3:
                        board[i][j] = 2
                else:
                    if liveCount < 2 or liveCount > 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0

    def countNeighborsLives(self, board, i, j):
        count = 0
        m, n = len(board), len(board[0])
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x = i + dx
                y = j + dy
                if x == i and y == j:
                    continue
                if 0 <= x < m and 0 <= y < n:
                    count += board[x][y] % 2 
        return count