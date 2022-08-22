# 1st solution
# O(1) time | O(1) space
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        while 4**x < n:
            x += 1
        
        return 4**x == n

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0 and 0b1010101010101010101010101010101 & n == n