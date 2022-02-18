# 1st solution
# O(n) time | O(n) space
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        stack = deque(["0"])
        i = 0
        while k > 0 and i < len(num):
            if num[i] < stack[-1]:
                stack.pop()
                k -= 1
            else:
                stack.append(num[i])
                i += 1

        while i < len(num):
            stack.append(num[i])
            i += 1

        while k > 0:
            k -= 1
            stack.pop()

        while len(stack) > 1 and stack[0] == "0":
            stack.popleft()

        return "".join(stack)