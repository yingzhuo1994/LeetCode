# 1st solution
# O(2^n) time | O(2^n) space
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        level = set([i for i in range(1, 10)])
        for i in range(1, n):
            newLevel = set()
            for num in level:
                d = num % 10
                if d + k < 10:
                    newLevel.add(num * 10 + d + k)
                if d - k >= 0:
                    newLevel.add(num * 10 + d - k)
            level = newLevel
        return list(level)