# 1st solution
# O(n) time | O(1) space
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        curTime = 0
        lastColor = ""
        for i, color in enumerate(colors):
            if color != lastColor:
                ans += curTime
                curTime = neededTime[i]
            else:
                curTime = max(curTime, neededTime[i])
            lastColor = color
        ans += curTime
        return sum(neededTime) - ans
    