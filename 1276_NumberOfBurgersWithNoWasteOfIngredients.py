# 1st solution
# O(1) time | O(1) space
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x, y = tomatoSlices, cheeseSlices
        if x & 1:
            return []
        a = x // 2 - y
        if a < 0:
            return []
        b = y - a
        if b < 0:
            return []
        return [a, b]