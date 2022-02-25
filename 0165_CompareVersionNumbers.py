# 1st solution
# O(n + m) time | O(n + m) space
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        stackOne = self.getStack(version1)
        stackTwo = self.getStack(version2)
        for i in range(min(len(stackOne), len(stackTwo))):
            if stackOne[i] < stackTwo[i]:
                return -1
            elif stackOne[i] > stackTwo[i]:
                return 1
        if len(stackOne) > len(stackTwo):
            return 1
        elif len(stackOne) < len(stackTwo):
            return -1
        else:
            return 0
    
    def getStack(self, version):
        stack = version.split(".")
        for i in range(len(stack)):
            stack[i] = int(stack[i])
        while len(stack) > 1 and stack[-1] == 0:
            stack.pop()
        return stack