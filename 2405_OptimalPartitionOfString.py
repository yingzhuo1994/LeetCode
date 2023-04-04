# 1st solution
# O(n) time | O(1) space
class Solution:
    def partitionString(self, s: str) -> int:
        start = -1
        count = 1
        dic = {}
        for i, ch in enumerate(s):
            if ch in dic and dic[ch] >= start:
                start = i
                count += 1
            dic[ch] = i
        return count