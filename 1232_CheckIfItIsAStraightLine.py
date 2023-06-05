# 1st solution
# O(n) time | O(1) space
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        A = y2 - y1
        B = x1 - x2
        C = y1 * x2 - x1 * y2
        return all(A * x + B * y + C == 0 for x, y in coordinates)
