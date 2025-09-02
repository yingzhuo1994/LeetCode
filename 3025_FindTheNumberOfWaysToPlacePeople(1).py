# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))  # x 升序，y 降序
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for (_, y2) in points[i + 1:]:
                if y1 >= y2 > max_y:
                    max_y = y2
                    ans += 1
        return ans
