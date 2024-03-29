class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pointSet = {(0, 0)}
        x, y = 0, 0
        for ch in path:
            if ch == "N":
                y += 1
            elif ch == "S":
                y -= 1
            elif ch == "W":
                x -= 1
            else:
                x += 1
            if (x, y) in pointSet:
                return True
            pointSet.add((x, y))
        return False
