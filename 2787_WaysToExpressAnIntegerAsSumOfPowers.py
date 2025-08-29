# 1st solution
# O((n^(1/x))!) time | O((n^(1/x))!) space
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        @cache
        def helper(val, m):
            if val < 0:
                return 0

            if val <= 1:
                print(val, m, 1)
                if val <= m:
                    return 1
                else:
                    0
            h = min(ceil(val**(1/x)), m)
            cnt = 0
            for i in reversed(range(1, h + 1)):
                cnt += helper(val - (i**x), i - 1)
            
            cnt %= MOD
            return cnt
        
        return helper(n, ceil(n**(1/x)))
    
# 2nd solution
# O(n * n^(1/x)) time | O(n) space
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        f = [1] + [0] * n
        for i in range(1, n + 1):
            v = i ** x
            if v > n:
                break
            for s in range(n, v - 1, -1):
                f[s] += f[s - v]
        return f[n] % 1_000_000_007