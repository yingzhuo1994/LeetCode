# 1st solution
# O(n) time | O(1) space
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0 # location
        dx, dy = 0, 1 # direction
        for ch in instructions:
            if ch == "G":
                x += dx
                y += dy
            elif ch == "L":
                dx, dy = -dy, dx
            elif ch == "R":
                dx, dy = dy, -dx

        if (dx, dy) == (0, 1):
            return (x, y) == (0 , 0)
        else:
            return True