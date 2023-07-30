# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def strangePrinter(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) <= 1:
            return 1
        
        n = len(s)
        state = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            state[i][i] = 1
        
        for i in reversed(range(n)):
            for dist in range(1, n - i):
                j = i + dist
                if dist == 1:
                    state[i][j] = 1 if s[i] == s[j] else 2
                    continue

                state[i][j] = float("inf")
                for k in range(i, j):
                    temp = state[i][k] + state[k + 1][j]
                    state[i][j] = min(state[i][j], temp)
                
                if s[i] == s[j]:
                    state[i][j] -= 1
        
        return state[0][n - 1]
