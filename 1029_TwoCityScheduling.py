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

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalCost = 0
        diffStack = []
        for a, b in costs:
            totalCost += a
            diffStack.append(b - a)
        
        diffStack.sort()
        totalCost += sum(diffStack[:len(costs) // 2])
        return totalCost

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalCost = 0
        diffStack = []
        for a, b in costs:
            totalCost += a
            diffStack.append(b - a)
        
        self.quickSelect(diffStack, 0, len(diffStack) - 1, len(diffStack) // 2)
        totalCost += sum(diffStack[:len(costs) // 2])
        return totalCost
    
    def quickSelect(self, nums, left, right, k):
        pivot = nums[left]
        L, R = left, right
        idx = L
        while idx <= R:
            if nums[idx] < pivot:
                self.swap(nums, L, idx)
                L += 1
                idx += 1
            elif nums[idx] > pivot:
                self.swap(nums, idx, R)
                R -= 1
            else:
                idx += 1
        if k <= L:
            return self.quickSelect(nums, left, L - 1, k)
        elif k > idx:
            return self.quickSelect(nums, idx, right, k)
        else:
            return pivot
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]