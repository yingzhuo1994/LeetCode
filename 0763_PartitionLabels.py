# 1st solution
# O(n) time | O(1) space
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastDic = {ch: i for i, ch in enumerate(s)}
        stack = []
        start = 0
        lastIdx = lastDic[s[0]]

        for i in range(len(s)):
            if i > lastIdx:
                stack.append(i - start)
                start = i
            lastIdx = max(lastIdx, lastDic[s[i]])
        if sum(stack) != len(s):
            stack.append(len(s) - start)
        return stack