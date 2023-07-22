# 1st solution
# O(k * n^2) time | O(n^2) space
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def getNeighbors(i, j):
            neighbors = []
            for dx, dy in [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n:
                    neighbors.append([x, y])
            return neighbors
        
        level = {(row, column): 1.0}
        while k > 0 and level:
            newLevel = {}
            for i, j in level:
                neighbors = getNeighbors(i, j)
                if not neighbors:
                    continue
                p = level[(i, j)]
                newP = p / 8
                for x, y in neighbors:
                    key = (x, y)
                    newLevel[key] = newLevel.get(key, 0) + newP
            level = newLevel
            k -= 1
        
        ans = 0
        for p in level.values():
            ans += p
        
        return ans
                
