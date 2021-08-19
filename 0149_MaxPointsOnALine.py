class Solution:
    # 1st solution
    # O(n^2) time | O(n^2) space
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        dic = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                lineParameters = self.getLineParameters(points[i], points[j])
                dic[lineParameters] = dic.get(lineParameters, 0)
        
        for i in range(len(points)):
            for lineParameters in dic:
                if self.check(lineParameters, points[i]):
                    dic[lineParameters] += 1
        return max(dic.values())
                    
    def getLineParameters(self, pointOne, pointTwo):
        x0, y0 = pointOne[0], pointOne[1]
        x1, y1 = pointTwo[0], pointTwo[1]
        if x0 == x1:
            return (1, 0, -x0)
        if y0 == y1:
            return (0, 1, -y0)
        return (y1 - y0, x0 - x1, x1 * y0 - x0 * y1)
    
    def check(self, lineParameters, point):
        A, B, C = lineParameters
        x, y = point[0], point[1]
        return A * x + B * y + C == 0