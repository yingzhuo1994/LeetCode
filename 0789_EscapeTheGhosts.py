# 1st solution
# O(n) time | O(1) space
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tagetDist = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            a = x - target[0]
            b = y - target[1]
            dist = abs(a) + abs(b)
            if dist <= tagetDist:
                return False
        return True