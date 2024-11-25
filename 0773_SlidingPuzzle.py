# 1st solution
# O(1) time | O(1) space
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def getStatus(board):
            return "".join(map(str, board[0] + board[1]))
        ans = "123450"
        memo = {}
        def move(key):
            for idx, ch in enumerate(key):
                if ch == "0":
                    break
            i, j = divmod(idx, 3)
            grid = [list(key[:3]), list(key[3:])]

            keys = set()
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < 2 and 0 <= y < 3:
                    grid[i][j], grid[x][y] = grid[x][y], grid[i][j]
                    keys.add(getStatus(grid))
                    grid[i][j], grid[x][y] = grid[x][y], grid[i][j]
            return keys
        visited = {getStatus(board)}
        q = deque([[getStatus(board), 0]])
        while q:
            key, step = q.popleft()
            if key == ans:
                return step
            keys = move(key)
            for key in keys:
                if key in visited:
                    continue
                visited.add(key)
                q.append([key, step + 1])
        return -1