# 1st solution
# O(kn) time | O(n) space
# where n = len(s), k is the parenthese pair number
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(ch)
        return "".join(stack)


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def reverseParentheses(self, s: str) -> str:
        opened = []
        pair = {}
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            if c == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)