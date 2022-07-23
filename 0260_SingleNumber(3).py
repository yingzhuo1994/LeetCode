# O(n) time | O(1) space
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = reduce(xor, nums)
        # nz is non-zero bit
        # s & s -1 is used to remove last 1
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)