# 1st solution, TLE
class Solution:
    def soupServings(self, n: int) -> float:
        plans = [[100, 0], [75, 25], [50, 50], [25, 75]]

        ans = 0

        state = {(n, n): 1.0}
        while state:
            newState = {}
            for key, p in state.items():
                A, B = key
                for a, b in plans:
                    leftA = A - a
                    leftB = B - b
                    if leftA <= 0:
                        if leftA < leftB:
                            ans += p * 0.25
                        elif leftA == leftB:
                            ans += 0.5 * p * 0.25
                    if leftA > 0 and leftB > 0:
                        newState[(leftA, leftB)] = newState.get((leftA, leftB), 0) + p * 0.25

            state = newState
        
        return ans

# 2nd solution
class Solution:
    def soupServings(self, n: int) -> float:
        memo = {}
        if n > 4800: 
            return 1
        def f(a, b):
            if (a, b) in memo: 
                return memo[a, b]
            if a <= 0 and b <= 0: 
                return 0.5
            if a <= 0: 
                return 1
            if b <= 0: 
                return 0
            
            memo[(a, b)] = 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))

            return memo[(a, b)]
        
        N = math.ceil(n / 25.0)
        
        return f(N, N)

# 3rd solution, bottom-up dp
# O(1) time | O(1) space
class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = {}

        def calculate_dp(i, j):
            return (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][j - 1] +
                    dp[max(0, i - 2)][max(0, j - 2)]
                    + dp[i - 1][max(0, j - 3)]) / 4

        dp[0] = {0: 0.5}
        for k in range(1, m + 1):
            dp[0][k] = 1
            dp[k] = {0: 0}
            for j in range(1, k + 1):
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)
            if dp[k][k] > 1 - 1e-5:
                return 1
        
        return dp[m][m]