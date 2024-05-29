# 1st solution
# O(n) time | O(n) space
class Solution:
    def numSteps(self, s: str) -> int:
        lst = list(s)[::-1]
        num = sum(int(lst[i]) * pow(2, i) for i in range(len(lst)))
        step = 0
        while num > 1:
            step += 1
            if num & 1:
                num += 1
            else:
                num >>= 1
        return step

