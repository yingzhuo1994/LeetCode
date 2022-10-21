class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        m = len(pizza)
        n = len(pizza[0])

        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(k, row, col):
            if preSum[row][col] == 0: return 0
            if k == 0: return 1
            ans = 0
            # cut horizontally
            for nr in range(row + 1, m):
                if preSum[row][col] - preSum[nr][col] > 0:
                    ans += dp(k - 1, nr, col)
            # cut vertically                    
            for nc in range(col + 1, n):
                if preSum[row][col] - preSum[row][nc] > 0:
                    ans += dp(k - 1, row, nc)
            ans %= MOD
            return ans

        return dp(k - 1, 0, 0)