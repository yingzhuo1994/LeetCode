# 1st solution
# O(n) time | O(1) space
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False
        lockedStack = []
        unlockedStack = []
        for i, ch in enumerate(s):
            if locked[i] == "0":
                unlockedStack.append(i)
                continue
            if ch == "(":
                lockedStack.append(i)
            else:
                if lockedStack:
                    lockedStack.pop()
                elif unlockedStack:
                    unlockedStack.pop()
                else:
                    return False
        while lockedStack and unlockedStack and lockedStack[-1] < unlockedStack[-1]:
            lockedStack.pop()
            unlockedStack.pop()
        return len(lockedStack) == 0