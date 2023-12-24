# 1st solution
# O(log(m)) time | O(1) space
# m = neededApples
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 0
        s = 0
        while s < neededApples:
            n += 1
            s += 12 * n**2
        return 8 * n