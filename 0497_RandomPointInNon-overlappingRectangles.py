import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects.copy()
        self.areas = self.calculateRatio()
        self.totalArea = self.areas[-1]
    
    def calculateRatio(self):
        n = len(self.rects)
        areas = []
        for a, b, x, y in self.rects:
            width =  x - a + 1
            height = y - b + 1
            s = width * height
            areas.append(s)
        for i in range(n - 1):
            areas[i+1] += areas[i]
        return areas

    def pick(self) -> List[int]:
        value = random.random() * self.totalArea
        idx = bisect.bisect_left(self.areas, value)
        a, b, x, y = self.rects[idx]
        u, v = random.randint(a, x), random.randint(b, y)
        return [u, v]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()