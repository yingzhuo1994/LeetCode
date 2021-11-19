# 1st solution
# O(1) time | O(1) space
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        print(bin(z))
        distance = 0
        while z > 0:
            distance += z & 1
            z >>= 1
        return distance