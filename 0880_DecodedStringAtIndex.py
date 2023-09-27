# 1st solution, MLE
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                d = int(ch)
                newStack = []
                for _ in range(d):
                    newStack.extend(stack)
                stack = newStack
            else:
                stack.append(ch)

            if len(stack) >= k:
                return stack[k - 1]