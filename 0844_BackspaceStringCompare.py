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

# 2nd solution
# O(s + t) time | O(1) space
# where s and t are string length
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i, s_ch = self.getNextIndexAndCh(s, i)
            j, t_ch = self.getNextIndexAndCh(t, j)
            if s_ch != t_ch:
                return False
        return i == j

    def getNextIndexAndCh(self, s, i):
        count = 0
        while i >= 0:
            if s[i] == "#":
                count += 1
                i -= 1
            elif count > 0:
                count -= 1
                i -= 1
            else:
                break
        if i < 0:
            return -1, ""
        else:
            return i - 1, s[i]