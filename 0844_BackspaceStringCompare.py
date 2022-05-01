# 1st solution
# O(s + t) time | O(s + t) space
# where s and t are string length
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = self.simplifyString(s)
        stack_t = self.simplifyString(t)
        if len(stack_s) != len(stack_t):
            return False
        for i in range(len(stack_s)):
            if stack_s[i] != stack_t[i]:
                return False
        return True 

    def simplifyString(self, s):
        stack = []
        for ch in s:
            if ch == "#":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ch)
        return stack