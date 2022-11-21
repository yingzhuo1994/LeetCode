# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        exits = []
        for i in range(m):
            if maze[i][0] == ".":
                if [i, 0] != entrance:
                    exits.append([i, 0])
            if n > 1:
                if maze[i][n-1] == ".":
                    if [i, n-1] != entrance:
                        exits.append([i, n-1])
        
        for j in range(n):
            if j == 0 or j == n - 1:
                continue
            if maze[0][j] == ".":
                if [0, j] != entrance:
                    exits.append([0, j])
            if m > 1:
                if maze[m - 1][j] == ".":
                    if [m - 1, j] != entrance:
                        exits.append([m - 1, j])
        
        if len(exits) == 0:
            return -1
        
        level = deque([[entrance[0], entrance[1], 0]])
        visited = set([(entrance[0], entrance[1])])
        while level:
            i, j, step = level.popleft()
            step += 1
            for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and maze[x][y] != "+":
                    if (x, y) not in visited:
                        if [x, y] in exits:
                            return step
                        visited.add((x, y))
                        level.append([x, y, step])
        return -1
