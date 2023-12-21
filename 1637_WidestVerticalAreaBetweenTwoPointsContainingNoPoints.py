# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xSet = set()
        for x, y in points:
            xSet.add(x)
        xList = sorted(list(xSet))
        ans = 0
        for i in range(len(xList) - 1):
            width = xList[i + 1] - xList[i]
            ans = max(ans, width)
        return ans
