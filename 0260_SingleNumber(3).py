class Solution:
    # O(n) time | O(1) space
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)