# 1st solution
# O(n * log(n)) time | O(1) space
import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if n - 1 >= hour:
            return -1
        
        def enough(speed):
            t = 0
            for i in range(n - 1):
                t += math.ceil(dist[i] / speed)
            t += dist[-1] / speed
            return t <= hour
        
        maxSpeed = math.ceil(dist[-1] / (hour - (n - 1)))
        for i in range(n - 1):
            maxSpeed = max(maxSpeed, dist[i])

        minSpeed = 1
        ans = maxSpeed
        while minSpeed < maxSpeed:
            speed = minSpeed + (maxSpeed - minSpeed) // 2
            if enough(speed):
                ans = speed
                maxSpeed = speed
            else:
                minSpeed = speed + 1
        return ans
