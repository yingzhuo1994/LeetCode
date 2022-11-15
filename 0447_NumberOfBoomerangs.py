# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            x0, y0 = points[i]
            dic = Counter()
            for j in range(len(points)):
                if j == i:
                    continue
                x1, y1 = points[j]
                dist = (x1 - x0)**2 + (y1 - y0)**2
                dic[dist] += 1
            for k in dic.values():
                ans += k * (k - 1)

        return ans