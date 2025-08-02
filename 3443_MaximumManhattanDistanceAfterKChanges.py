# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        N = S = W = E = 0
        ans = 0
        for ch in s:
            if ch == "W":
                W += 1
            elif ch == "E":
                E += 1
            elif ch == "S":
                S += 1
            else:
                N += 1
            x = E - W
            y = N - S
            x2 = min(W, E)
            y2 = min(N, S)
            dist = abs(x) + abs(y) + 2 * min(x2 + y2, k)
            ans = max(ans, dist)
        return ans
