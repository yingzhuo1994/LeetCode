# 1st solution
# O(n) time | O(n) space
class Solution:
    def decodeString(self, s: str) -> str:
        num, stack = 0, [""]
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append(num)
                num = 0
                stack.append("")
            elif ch == "]":
                str1 = stack.pop()
                rep = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1 * rep)
            else:
                stack[-1] += ch                         
        return "".join(stack)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def decodeString(self, s: str) -> str:
        num, stack = 0, [[]]
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append(num)
                num = 0
                stack.append([])
            elif ch == "]":
                last = stack.pop()
                rep = stack.pop()
                stack[-1] += rep * last
            else:
                stack[-1].append(ch)                         
        return "".join(stack[0])