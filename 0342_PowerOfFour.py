# 1st solution
# O(1) time | O(1) space
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        while 4**x < n:
            x += 1
        
        return 4**x == n