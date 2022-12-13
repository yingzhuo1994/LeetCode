# 1st solution, TLE
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        def helper(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left >= right:
                memo[(left, right)] = 0
                return 0
            ans = float("inf")
            for i in range(left, right + 1):
                leftVal = helper(left, i - 1)
                rightVal = helper(i + 1, right)
                ans = min(ans, max(leftVal, rightVal) + i)
            memo[(left, right)] = ans
            return ans
        return helper(1, n)
