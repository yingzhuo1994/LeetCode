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

# 2nd solution
# O(n) time | o(n) space
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = [[], 0]
        for ch in s:
            if ch.isdigit():
                d = int(ch)
                stack = [stack, stack[1] * d]
            else:
                stack[0].append(ch)
                stack[1] += 1

            if stack[1] >= k:
                break

        def dfs(stack, k):
            last, n = stack
            left = 0
            m = None
            for i in reversed(range(len(last))):
                ch = last[i]
                if type(ch) is int:
                    m = ch
                    break
                left += 1
            if m is None:
                return last[k- 1]
            repeat = (n - left) // m
            r = k - repeat * m
            if r > 0:
                return last[i + r]
            else:
                return dfs(last[:i+1], (k - 1) % m + 1)

        return dfs(stack, k)