# 1st solution, TLE
# O(3^n) time | O(n) space
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

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def numTrees(self, n: int) -> int:
        self.numDic = {-1: 1}
        result = self.numTreesWithRange(1, n)
        print(self.numDic)
        return result

    def numTreesWithRange(self, lower, upper):
        diff = upper - lower
        if diff in self.numDic:
            return self.numDic[diff]
        count = 0
        for i in range(lower, upper + 1):
            count += self.numTreesWithRange(lower, i - 1) * self.numTreesWithRange(i + 1, upper)
        self.numDic[diff] = count
        return count

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)