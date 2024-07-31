# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        x_set = set([point[0] for point in points])
        if w == 0:
            return len(x_set)
        x_list = list(x_set)
        x_list.sort()
        ans = 1
        start_x = x_list[0]
        for i in range(1, len(x_list)):
            if x_list[i] - start_x > w:
                ans += 1
                start_x = x_list[i]
        return ans