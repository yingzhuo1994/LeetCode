# 1st solution
# O(1) time | O(1) space
class Solution:
    def binaryGap(self, n: int) -> int:
        s = str(bin(n))[2:]
        last = -1
        ans = 0
        for i, ch in enumerate(s):
            if ch == "1":
                if last >= 0:
                    ans = max(ans, i - last)
                last = i
        return ans