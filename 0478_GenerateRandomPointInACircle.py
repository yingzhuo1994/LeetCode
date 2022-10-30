# 1st solution
# O(1) time | O(1) space
import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
        
    def randPoint(self) -> List[float]:
        while True:
            dx = (random.random() - 0.5) * 2 * self.radius 
            dy = (random.random() - 0.5) * 2 * self.radius
            if dx**2 + dy**2 <= self.radius**2:
                return [self.x_center + dx, self.y_center + dy]

# 2nd solution
# O(1) time | O(1) space
import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
        
    def randPoint(self) -> List[float]:
        theta = random.uniform(0, 2 * math.pi)
        r = math.sqrt(random.uniform(0, 1)) * self.radius
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()