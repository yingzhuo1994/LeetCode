# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        def updateStack(left, right):
            a1, b1 = bisectSearch(left)
            a2, b2 = bisectSearch(right)
            start = a1
            end = b2
            middleStack = []
            highest = 0
            for idx in range(start, end):
                if stack[idx][1] > highest:
                    highest = stack[idx][1]
            hight = highest + right - left
            if stack[start][0] < left:
                middleStack.append(stack[start])
            middleStack.append([left, hight])
            middleStack.append([right, stack[end - 1][1]])
            if stack[end][0] > right:
                middleStack.append(stack[end])
            else:
                middleStack[-1][1] = max(middleStack[-1][1], stack[end][1])

            stack[start:end+1] = middleStack
            return hight
        
        def bisectSearch(x):
            start, end = 0, len(stack) - 1
            while start < end:
                mid = start + (end - start) // 2
                if stack[mid][0] <= x:
                    a = mid
                    start = mid + 1
                else:
                    end = mid
            
            start, end = 0, len(stack) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if stack[mid][0] >= x:
                    b = mid 
                    end = mid - 1
                else:
                    start = mid + 1
            
            return a, b
        
        stack = [[0, 0], [float('inf'), 0]]
        ans = []
        highest = 0
        for left, sideLength in positions:
            right = left + sideLength
            h = updateStack(left, right)
            highest = max(highest, h)
            ans.append(highest)
        return ans