# 1st solution
# O(n*log(n)) time | O(1) space
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda v: v[1])
        count = 1
        cur = points[0]

        for i in range(len(points)):
            if cur[1] < points[i][0]:
                count += 1
                cur = points[i]
        return count