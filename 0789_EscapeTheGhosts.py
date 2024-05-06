# 1st solution
# O(n) time | O(1) space
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x, y = target
        tagetDist = abs(x) + abs(y)
        return all(tagetDist < abs(x - a) + abs(y - b) for a, b in ghosts)