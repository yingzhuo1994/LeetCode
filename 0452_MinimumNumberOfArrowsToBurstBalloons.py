# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda v: v[1])
        self.table = [False for _ in points]
        self.ans = 0
        self.dfs(points, 0)

        return self.ans
    
    def dfs(self, points, start):
        self.table[start] = True
        end = points[start][1]
        self.ans += 1

        for i in range(start + 1, len(points)):
            if self.table[i]:
                continue
            if points[i][0] <= end <= points[i][1]:
                self.table[i] = True
            else:
                self.dfs(points, i,)
                break