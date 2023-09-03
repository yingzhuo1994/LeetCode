# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        monsters = [dist[i] / speed[i] for i in range(n)]
        monsters.sort()

        count = 0
        for i, t in enumerate(monsters):
            if t <= i:
                return count
            else:
                count += 1
        return count
            