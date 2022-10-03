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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = max_cost = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                max_cost = 0
            res += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])
        return res