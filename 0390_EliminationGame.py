# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def lastRemaining(self, n: int) -> int:
        stack = [i for i in range(1, n + 1)]
        step = 2
        while len(stack) > 1:
            newStack = []
            if step > 0:
                i = 1
            else:
                i = len(stack) - 2
            
            while 0 <= i < len(stack):
                newStack.append(stack[i])
                i += step
            if step < 0:
                newStack.reverse()
            step *= -1
            stack = newStack
        return stack[0]
            
# 2nd solution
# O(log(n)) time | O(1) space
class Solution:
    def lastRemaining(self, n: int) -> int:
        stack = [1, n, 1]
        direction = 1
        while stack[0] != stack[1] > 1:
            step = stack[2]
            newStep = step * 2
            if direction > 0:
                start = stack[0] + step
                count = (stack[1] - start) // newStep
                end = min(stack[1], start + count * newStep)
            else:
                end = stack[1] - step
                count = (end - stack[0]) // newStep
                start = max(stack[0], end -  count * newStep)
            direction *= -1
            stack = [start, end, newStep]
        return stack[0]

# 3rd solution
# O(log(n)) time | O(1) space
class Solution:
    def lastRemaining(self, n: int) -> int:
        isLeft = True
        remaining = n
        step = 1
        head = 1
        while remaining > 1:
            if isLeft or remaining & 1:
                head = head + step
            remaining >>= 1
            step *= 2
            isLeft = not isLeft
        return head