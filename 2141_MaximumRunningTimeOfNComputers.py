# 1st solution
# O(m * log(m)) time | O(m) space
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total = sum(batteries)

        while batteries[-1] > total // n:
            n -= 1
            total -= batteries.pop()
        return total // n