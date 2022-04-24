class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for circle in circles:
            self.addPoints(points, circle)
        return len(points)
    
    def addPoints(self, points, circle):
        x, y, r = circle
        for dx in range(-r, r+1):
            for dy in range(-r, r+1):
                a = x + dx
                b = y + dy
                if dx**2 + dy**2 <= r**2:
                    points.add((a, b))
        return points
    

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        circles.sort(key = lambda v: v[2])
        maxRidus = circles[-1][2]
        newCircles = defaultdict(set)
        for i in reversed(range(len(circles))):
            if self.isContained(newCircles, circles[i]):
                continue
            elem = (circles[i][0], circles[i][1], circles[i][2])
            newCircles[circles[i][2]].add(elem)
        print(newCircles)
        points = set()
        ridius = sorted(newCircles.keys())
        for r in ridius:
            for circle in newCircles[r]:
                self.addPoints(points, circle)
        return len(points)
    
    def addPoints(self, points, circle):
        x, y, r = circle
        for dx in range(-r, r+1):
            for dy in range(-r, r+1):
                a = x + dx
                b = y + dy
                if dx**2 + dy**2 <= r**2:
                    points.add((a, b))
        return points
    
    def isContained(self, newCircles, circle):
        x, y, r = circle
        ridius = sorted(newCircles.keys())
        # left, right = 0, len(ridius) - 1
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if ridius[mid] <= r:
        #         left = mid + 1
        #     else:
        #         right = mid - 1


        for i in range(len(ridius)):
            if ridius[i] <= r:
                continue
            for a, b, c in newCircles[ridius[i]]:
                if (x - a)**2 + (y - b)**2 <= (c -r)**2:
                    return True
        return False
