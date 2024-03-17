# 1st solution
# O(n) time | O(1) space
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count