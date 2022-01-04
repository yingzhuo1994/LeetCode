# 1st solution
# O(1) time | O(1) space
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        k = 1
        while k < n:
            k = (k << 1) | 1
        return k - n