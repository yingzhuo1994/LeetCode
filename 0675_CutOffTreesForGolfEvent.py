# 1st solution, MLE
# O((mn)^2) time | O((mn)^2) space
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        dic = {}
        def query(i, j):
            if (i, j) in dic:
                return dic[(i, j)]
            if i == j:
                return 0
            
            dist = float("inf")
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    k = x * n + y
                    newDist = query(k, j) + 1
                    dist = min(dist, newDist)
            dic[(i, j)] = dist

            return dist
        
        cost = 0
        lst = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    lst.append([forest[i][j], i * n + j])
        lst.sort()
        last = 0
        for _, j in lst:
            dist = query(last, j)
            if dist == float("inf"):
                return -1
            cost += dist
            last = j
        
        return cost
