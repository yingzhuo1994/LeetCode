class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(1) time | O(1) space
        count = 0
        while n:
            if (n & 1) == 1:
                count += 1
            n = n >> 1
        return count
