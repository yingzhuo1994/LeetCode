# 1st solution
# O(2^m*n*m) time | O(4^m) space
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        dp, MOD = {(1<<(2*m)) - 1: 1}, 10**9 + 7
        
        for index in range(m*n-1, -1, -1):
            dp2 = Counter()
            R, C = divmod(index, m)
            
            for row in dp:
                allowed = {0, 1, 2}
                if C < m - 1: allowed.discard(row >> (2*m-2))
                if R < n - 1: allowed.discard(row & 3)

                for val in allowed:
                    row2 = (row >> 2) + (val<<(2*m-2))
                    dp2[row2] = (dp2[row2] + dp[row]) % MOD 
            
            dp = dp2
    
        return sum(dp.values()) % MOD