# 1st solution
# O(n) time | O(n) space
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        lst = preorder.split(",")
        n = len(lst)
        if n == 0:
            return True

        if lst[0] == "#":
            return n == 1

        stack = [[lst[0], 0]]
        for i in range(1, n):
            if not stack:
                return False
            stack[-1][1] += 1
            if stack[-1][1] > 2:
                return False
            if lst[i] != "#":
                stack.append([lst[i], 0])
            while stack and stack[-1][1] == 2:
                stack.pop()

        return len(stack) == 0