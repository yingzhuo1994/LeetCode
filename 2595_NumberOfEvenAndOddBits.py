# 1st solution
# O(1) time | O(1) space
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        k = 0
        while n > 0:
            if n & 1:
                if k & 1:
                    odd += 1
                else:
                    even += 1
            n >>= 1
            k += 1
        return [even, odd]