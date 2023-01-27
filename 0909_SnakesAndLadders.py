# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getLocation(num):
            k, r = divmod(num - 1, n)
            if k & 1:
                y = n - 1 - r
            else:
                y = r
            x = n - 1 - k
            return x, y

        level = [1]
        visited = set([1])
        step = 0
        while level:
            newLevel = []
            step += 1
            for num in level:
                for k in range(num + 1, min(num + 6, n**2) + 1):
                    if k in visited:
                        continue
                    visited.add(k)
                    x, y = getLocation(k)
                    if board[x][y] != -1:
                        new = board[x][y]
                    else:
                        new = k

                    if new == n**2:
                        return step

                    newLevel.append(new)
            level = newLevel

        return -1

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getLocation(num):
            k, r = divmod(num - 1, n)
            if k & 1:
                y = n - 1 - r
            else:
                y = r
            x = n - 1 - k
            return x, y

        level = [1]
        step = 0
        while level:
            newLevel = []
            step += 1
            for num in level:
                for k in range(num + 1, min(num + 6, n**2) + 1):
                    x, y = getLocation(k)
                    if board[x][y] == 0:
                        continue
                    elif board[x][y] == -1:
                        new = k
                    else:
                        new = board[x][y]
                    
                    board[x][y] = 0
                    if new == n**2:
                        return step
                    
                    newLevel.append(new)
            level = newLevel
        return -1

# 3rd solution, optimized
# O(n^2) time | O(n) space
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getLocation(num):
            k, r = divmod(num - 1, n)
            if k & 1:
                y = n - 1 - r
            else:
                y = r
            x = n - 1 - k
            return x, y

        level = [1]
        step = 0
        while level:
            newLevel = []
            step += 1
            for num in level:
                for k in reversed(range(num + 1, min(num + 6, n**2) + 1)):
                    x, y = getLocation(k)
                    if board[x][y] == -1:
                        newLevel.append(k)
                        break
                for k in range(num + 1, min(num + 6, n**2) + 1):
                    x, y = getLocation(k)
                    if board[x][y] == 0:
                        continue
                    elif board[x][y] == -1:
                        new = k
                    else:
                        new = board[x][y]
                        newLevel.append(new)
                    
                    board[x][y] = 0
                    if new == n**2:
                        return step
                    
            level = newLevel
        return -1