# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float("inf")
        pointsSet = set([(x ,y) for x, y in points])
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                A = (x1, y2)
                B = (x2, y1)
                if A not in pointsSet or B not in pointsSet:
                    continue
                area = abs(x1 - x2) * abs(y1 - y2)
                ans = min(ans, area)
        return ans if ans != float("inf") else 0