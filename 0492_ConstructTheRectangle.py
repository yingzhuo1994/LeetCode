# 1st solution
# O(sqrt(area)) time | O(1) space
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for W in reversed(range(1, int(math.sqrt(area)) + 1)):
            if area % W != 0:
                continue
            L = area // W
            return [L, W]