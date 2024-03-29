class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        
        mask = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign. 
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer. 
        # a ^ b gets the summation without a carry
        # a & b gets the carry result
        # mask keeps the sign
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a &= mask
        b &= mask
        while b:
            carry = (a & b) << 1
            a ^= b
            b = carry & mask
            # print((a, b))
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a