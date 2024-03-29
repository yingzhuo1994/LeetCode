# 1st recursive solution
# O(mn) time | O(m + n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        toRight = self.uniquePaths(m, n - 1)
        toBottom = self.uniquePaths(m - 1, n)
        return toRight + toBottom

# 2nd iterative solution
# O(mn) time | O(n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        ways = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                ways[j] = ways[j] + ways[j - 1]
        return ways[-1]

# 3nd math solution
# O(mn) time | O(1) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(n):
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        
        a = m - 1
        b = n - 1
        return factorial(a + b) // (factorial(a) * factorial(b))

