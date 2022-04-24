# 1st solution
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for circle in circles:
            self.addPoints(points, circle)
        return len(points)
    
    def addPoints(self, points, circle):
        x, y, r = circle
        for cx in range(x + 1, x + r + 1):
            for cy in range(y + 1, y + r + 1):
                if math.sqrt((cx-x)**2 + (cy-y)**2) <= r:
                    points.add((cx, cy))
                    points.add((2*x-cx, cy))
                    points.add((2*x-cx, 2*y-cy))
                    points.add((cx, 2*y-cy))
        for cy in range(y-r,y+r+1): points.add((x,cy))
        for cx in range(x-r,x+r+1): points.add((cx,y))

# 2nd solution
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        circles.sort(key = lambda v: v[2])
        newCircles = defaultdict(set)
        for i in reversed(range(len(circles))):
            if self.isContained(newCircles, circles[i]):
                continue
            elem = (circles[i][0], circles[i][1], circles[i][2])
            newCircles[circles[i][2]].add(elem)

        points = set()
        for r in newCircles:
            for circle in newCircles[r]:
                self.addPoints(points, circle)
        return len(points)
    
    def addPoints(self, points, circle):
        x, y, r = circle
        for cx in range(x + 1, x + r + 1):
            for cy in range(y + 1, y + r + 1):
                if math.sqrt((cx-x)**2 + (cy-y)**2) <= r:
                    points.add((cx, cy))
                    points.add((2*x-cx, cy))
                    points.add((2*x-cx, 2*y-cy))
                    points.add((cx, 2*y-cy))
        for cy in range(y-r,y+r+1): points.add((x,cy))
        for cx in range(x-r,x+r+1): points.add((cx,y))
    
    def isContained(self, newCircles, circle):
        x, y, r = circle
        ridius = sorted(newCircles.keys())

        for i in range(len(ridius)):
            if ridius[i] <= r:
                continue
            for a, b, c in newCircles[ridius[i]]:
                if (x - a)**2 + (y - b)**2 <= (c -r)**2:
                    return True
        return False
