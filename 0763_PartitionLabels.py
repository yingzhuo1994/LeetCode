# 1st solution
# O(n) time | O(1) space
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastDic = {ch: i for i, ch in enumerate(s)}
        stack = []
        start = 0
        lastIdx = 0

        for i in range(len(s)):
            lastIdx = max(lastIdx, lastDic[s[i]])
            if i == lastIdx:
                stack.append(i - start + 1)
                start = i + 1

        return stack