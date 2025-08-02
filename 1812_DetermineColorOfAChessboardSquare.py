# 1st solution
# O(1) time | O(1) space
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord("a")
        y = int(coordinates[1]) - 1
        z = x + y
        return True if z & 1 else False