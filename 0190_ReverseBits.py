# O(1) time | O(1) space
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n > 0:
            ret |= (n & 1) << power
            n >>= 1
            power -= 1
        return ret
