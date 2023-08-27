# 1st solution, MLE
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        stack = [[n, 1]]
        ans = 1
        while stack:
            newStack = []
            for left, k in stack:
                if left == k:
                    return ans
                elif left > k:
                    newStack.append([left - k, k])
                    newStack.append([left, n - left])
            ans += 1
            stack = newStack

# 2nd solution
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        @cache
        def dfs(left, k):
            if left == 0:
                return 0
            elif left == k:
                return 1
            elif left < k:
                return float("inf")
            ans = dfs(left - k, k)
            if n - left > k:
                ans = min(ans, dfs(left, n - left))
            return ans + 1
        
        return dfs(n, 1)

# 3rd solution
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            while n % i == 0:
                ans += i
                n = n // i
        return ans