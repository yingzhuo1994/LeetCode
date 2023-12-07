# 1st solution
# O(n) time | O(1) space
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) & 1:
                return num[:i+1]
        return ""