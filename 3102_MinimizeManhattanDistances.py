# 1st solution
# O(n * log(n)) time | O(n) space
from sortedcontainers import SortedList
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        x_plus_y = SortedList()
        y_minus_x = SortedList()
        for x, y in points:
            x_plus_y.add(x + y)
            y_minus_x.add(y - x)

        ans = inf
        for a, b in points:
            x, y = a + b, b - a
            x_plus_y.remove(x)
            y_minus_x.remove(y)
            ans = min(ans, max(x_plus_y[-1] - x_plus_y[0], y_minus_x[-1] - y_minus_x[0]))
            x_plus_y.add(x)
            y_minus_x.add(y)
        return ans