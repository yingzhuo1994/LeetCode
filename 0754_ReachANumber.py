# 1st solution, BFS, TLE
class Solution:
    def reachNumber(self, target: int) -> int:
        level = set([0])
        step = 1
        while level:
            newLevel = set()
            for p in level:
                newLevel.add(p + step)
                newLevel.add(p - step)
            level = newLevel
            if target in level:
                return step
            step += 1
        