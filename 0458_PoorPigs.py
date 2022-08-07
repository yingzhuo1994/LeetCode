# 1st solution
# O(1) time | O(1) space
from math import log2
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        t = minutesToTest // minutesToDie
        x = 1
        while (t + 1)**x < buckets:
            x += 1
        return x