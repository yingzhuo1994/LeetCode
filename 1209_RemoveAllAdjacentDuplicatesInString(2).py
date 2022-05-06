# 1st solution
# O(n) time | O(n) space
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["", 0]]
        for i, ch in enumerate(s):
            if ch == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        return self.makeNewString(stack)
    
    def makeNewString(self, stack):
        stringStack = []
        for ch, count in stack:
            stringStack.append(ch * count)
        return "".join(stringStack)
            