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

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def reachNumber(self, target: int) -> int:
        t = abs(target)
        x = int(-1 + math.sqrt(1 + 8 * t)) // 2

        while True:
            diff = (x + 1) * x // 2 - t
            if diff < 0 or diff & 1:
                x += 1
                continue
            else:
                return x

# 3rd solution
# O(1) time | O(1) space
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = n = 0
        while s < target or (s - target) % 2:  # 没有到达（越过）终点，或者相距奇数
            n += 1
            s += n
        return n