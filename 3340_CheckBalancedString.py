# 1st solution
# O(n) time | O(1) space
class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0
        for i, ch in enumerate(num):
            if i & 1:
                odd += int(ch)
            else:
                even += int(ch)
        return odd == even