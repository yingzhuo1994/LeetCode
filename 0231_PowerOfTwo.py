class Solution:
    # 1st solution
    # O(1) time | O(1) space  
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n

    # 2nd solution
    # O(1) time | O(1) space
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)