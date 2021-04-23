class Solution:
    def reverseBits(self, n: int) -> int:
        # O(1) time | O(1) space
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
