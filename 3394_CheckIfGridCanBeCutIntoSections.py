# 1st solution
# O(n * log(n)) time | O(n)
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontals = []
        verticals = []
        for x1, y1, x2, y2 in rectangles:
            horizontals.append([x1, x2])
            verticals.append([y1, y2])
        horizontals.sort(key=lambda v: [v[0], -v[1]])
        verticals.sort(key=lambda v: [v[0], -v[1]])

        def check(intervals):
            cnt = 0
            last = intervals[0][1]
            for a, b in intervals:
                if a >= last:
                    cnt += 1
                    last = b
                elif b >= last:
                    last = b
            return cnt >= 2
        
        return check(horizontals) or check(verticals)