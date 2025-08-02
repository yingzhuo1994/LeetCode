# 1st solution
# O(n) time | O(n) space
class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s) - 1):
            num1 = int(s[i])
            num2 = int(s[i + 1])
            if (num1 & 1) ^ (num2 & 1):
                continue
            if num1 > num2:
                ans = s[:i] + s[i + 1] + s[i] + s[i+2:]
                return ans
        return s