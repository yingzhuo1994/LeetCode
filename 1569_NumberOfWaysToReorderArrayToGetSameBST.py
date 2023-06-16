# 1st solution, TLE
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def helper(m, n):
            if n <= 0 or m <= 0:
                return 1
            if m == 1:
                return n + 1
            if m > n:
                m, n = n, m
            ans = 0
            for i in range(n + 1):
                ans += helper(m - 1, n - i)

            return ans

        def dfs(array):
            if len(array) <= 1:
                return 1
            
            value = array[0]
            left = [num for num in array if num < value]
            right = [num for num in array if num > value]
            leftCount = dfs(left)
            rightCount = dfs(right)
            count = leftCount * rightCount * helper(len(left), len(right)) % MOD
            return count
        
        
        return dfs(nums) - 1

# 2nd solution
# O(n^2 time) | O(n^2) space
# n = len(nums)
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def f(m, n):
            if n <= 0 or m <= 0:
                return 1
            if m == 1:
                return n + 1
            if m > n:
                m, n = n, m
            return f(m - 1, n) + f(m, n - 1)

        def dfs(array):
            if len(array) <= 1:
                return 1
            value = array[0]
            left = [num for num in array if num < value]
            right = [num for num in array if num > value]
            leftCount = dfs(left)
            rightCount = dfs(right)

            count = leftCount * rightCount * f(len(left), len(right)) % MOD
            return count
        
        return dfs(nums) - 1

# 3rd solution
# O(n^2 time) | O(n^2) space
# n = len(nums)
import math
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def f(m, n):
            x = m + n
            return math.factorial(x) // (math.factorial(m) * math.factorial(n))

        def dfs(array):
            if len(array) <= 1:
                return 1
            value = array[0]
            left = [num for num in array if num < value]
            right = [num for num in array if num > value]
            leftCount = dfs(left)
            rightCount = dfs(right)

            count = leftCount * rightCount * f(len(left), len(right)) % MOD
            return count
        
        return dfs(nums) - 1