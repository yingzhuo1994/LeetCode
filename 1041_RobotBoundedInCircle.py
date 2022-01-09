# 1st solution
# O(n) time | O(1) space
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        place = [0, 0]
        direction = (0, 1)
        turnLeft ={(0, 1): (-1, 0),
                   (-1, 0): (0, -1),
                   (0, -1): (1, 0),
                   (1, 0): (0, 1)
                   }
        turnRight = {(0, 1): (1, 0),
                     (1, 0): (0, -1),
                     (0, -1): (-1, 0),
                     (-1, 0): (0, 1)
                    }
        for ch in instructions:
            if ch == "G":
                place[0] += direction[0]
                place[1] += direction[1]
            elif ch == "L":
                direction = turnLeft[direction]
            elif ch == "R":
                direction = turnRight[direction]

        if direction == (0, 1):
            return place == [0, 0]
        else:
            return True