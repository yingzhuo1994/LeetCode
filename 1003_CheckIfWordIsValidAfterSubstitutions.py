# 1st solution
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) < 3:
            return False
        idx = s.find("abc")
        if idx < 0:
            return False
        return self.isValid(s[:idx] + s[idx+3:])

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return not stack