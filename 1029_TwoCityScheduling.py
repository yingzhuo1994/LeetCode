# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        stack = []
        for i, cost in enumerate(costs):
            stack.append([cost[1] - cost[0], i])
        stack.sort(key = lambda v: v[0])
        leftIdx, rightIdx = 0, len(costs) - 1
        leftCount, rightCount = 0, 0
        totalCost = 0
        while leftIdx <= rightIdx:
            leftDiff = abs(stack[leftIdx][0])
            rightDiff = abs(stack[rightIdx][0])

            if leftCount == len(costs) // 2 or (rightCount < len(costs) // 2 and leftDiff >= rightDiff):
                totalCost += costs[stack[leftIdx][1]][1]
                rightCount += 1
                leftIdx += 1
            else:
                totalCost += costs[stack[rightIdx][1]][0]
                leftCount += 1
                rightIdx -= 1
        return totalCost
