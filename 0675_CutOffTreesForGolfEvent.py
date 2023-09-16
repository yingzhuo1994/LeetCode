# 1st solution
# O((mn)^2) time | O((mn)^2) space
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        def query(x1, y1, x2, y2):
            if (x1, y1) == (x2, y2):
                return 0
            
            stack = [[x1, y1]]
            visited = set([(x1, y1)])
            dist = 1
            while stack:
                newStack = []
                for a, b in stack:
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        x = a + dx
                        y = b + dy
                        if 0 <= x < m and 0 <= y < n and forest[x][y] >= 1 and (x, y) not in visited:
                            if (x, y) == (x2, y2):
                                return dist
                            newStack.append([x, y])
                            visited.add((x, y))
                dist += 1
                stack = newStack
            
            return float("inf")
        
        cost = 0
        lst = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    lst.append([forest[i][j], i, j])
        lst.sort()
        last = [0, 0]
        for _, i, j in lst:
            dist = query(last[0], last[1], i, j)
            if dist == float("inf"):
                return -1
            cost += dist
            last = [i, j]
        
        return cost