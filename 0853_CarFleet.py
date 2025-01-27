# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = [i for i in range(n)]
        cars.sort(key=lambda idx: position[idx])
        ans = 1
        lastTime = (target - position[cars[-1]]) / speed[cars[-1]]
        for i in reversed(range(n - 1)):
            t = (target - position[cars[i]]) / speed[cars[i]]
            if t > lastTime:
                ans += 1
                lastTime = t
        return ans