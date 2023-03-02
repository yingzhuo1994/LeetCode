# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def getNeighbors(i, j):
            neighbors = set()
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) != (i, j):
                        neighbors.add((x, y))
            return neighbors

        def countMine(i, j):
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "M":
                        count += 1
            return count

        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            level = set([(x, y)])
            while level:
                newLevel = set()
                for x, y in level:
                    if board[x][y] in ("M", "B") or board[x][y].isdgit():
                        continue
                    count = countMine(x, y)
                    if count == 0:
                        board[x][y] = "B"
                        neighbors = getNeighbors(x, y)
                        for node in neighbors:
                            if node not in level:
                                newLevel.add(node)
                    else:
                        board[x][y] = str(count)
                level = newLevel
        return board
