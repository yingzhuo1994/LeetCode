# 1st solution, TLE
class Solution:
    def numTrees(self, n: int) -> int:
        return self.numTreesWithRange(1, n)

    def numTreesWithRange(self, lower, upper):
        if lower >= upper:
            return 1
        count = 0
        for i in range(lower, upper + 1):
            count += self.numTreesWithRange(lower, i - 1) * self.numTreesWithRange(i + 1, upper)
        return count
