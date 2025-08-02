# 1st solution
# O(1) time | O(1) space
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = len(board)
        x, y = 0, 0
        isFound = False
        for i in range(n):
            if isFound:
                break
            for j in range(n):
                if board[i][j] == "R":
                    x, y = i, j
                    isFound = True
                    break
        
        ans = 0
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            i, j = x, y
            while 0 <= i < n and 0 <= j < n:
                if board[i][j] == "p":
                    ans += 1
                    break
                elif board[i][j] == "B":
                    break
                i += dx
                j += dy
        return ans
