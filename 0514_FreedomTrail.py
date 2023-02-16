# 1st solution
# O(n^2 * m) time | O(n) space
# where n = len(ring) and m = len(key)
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        table = defaultdict(list)
        for i, ch in enumerate(ring):
            table[ch].append(i)
        n = len(ring)
        ans = len(key)
        stack = {(ring[0], 0): 0}
        for goal in key:
            newStack = {}
            for ch, i in stack:
                step = stack[(ch, i)]
                for j in table[goal]:
                    if j >= i:
                        dist = min(j - i, i + n - j)
                    else:
                        dist = min(i - j, j + n - i)
                    k = (goal, j)
                    newStep = step + dist
                    if k not in newStack or newStep < newStack[k]:
                        newStack[k] = newStep
            stack = newStack
        
        return ans + min(stack.values())