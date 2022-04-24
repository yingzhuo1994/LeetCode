class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        x_max = max(rectangles, key = lambda v: v[0])[0]
        y_max = max(rectangles, key = lambda v: v[1])[1]
        dp = [[0 for _ in range(y_max + 2)] for _ in range(x_max + 2)]
        for x, y in rectangles:
            dp[x][y] = 1

        for x in reversed(range(1, x_max + 1)):
            for y in reversed(range(1, y_max + 1)):
                dp[x][y] += dp[x + 1][y] + dp[x][y + 1] - dp[x + 1][y + 1]

        ans = []
        for x, y in points:
            if x <= x_max and y <= y_max:
                ans.append(dp[x][y])
            else:
                ans.append(0)
        
        return ans

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        xValues = set()
        yValues = set()
        dp = {}
        for x, y in rectangles:
            xValues.add(x)
            yValues.add(y)
        
        xValues = sorted(list(xValues))
        yValues = sorted(list(yValues))

        for x in xValues:
            for y in yValues:
                dp[(x, y)] = 0
        
        for x, y in rectangles:
            dp[(x, y)] = 1
        
        x = xValues[-1]
        for i in reversed(range(len(yValues) - 1)):
            y = yValues[i]
            dp[(x, y)] += dp[(x, yValues[i + 1])]

        y = yValues[-1]
        for i in reversed(range(len(xValues) - 1)):
            x = xValues[i]
            dp[(x, y)] += dp[(xValues[i + 1], y)]

        for i in reversed(range(len(xValues) - 1)):
            for j in reversed(range(len(yValues) - 1)):
                dp[(xValues[i], yValues[j])] += dp[(xValues[i], yValues[j + 1])] + dp[(xValues[i + 1], yValues[j])] - dp[(xValues[i + 1], yValues[j + 1])]

        ans = []
        for x, y in points:
            i = self.search(xValues, x)
            j = self.search(yValues, y)
            if i == len(xValues) or j == len(yValues):
                ans.append(0)
            else:
                ans.append(dp[(xValues[i], yValues[j])])
        
        return ans
    
    def search(self, array, value):
        left, right = 0, len(array)
        while left < right:
            mid = left + (right - left) // 2
            if array[mid] < value:
                left = mid + 1
            elif array[mid] > value:
                right = mid
            else:
                return mid
        return left