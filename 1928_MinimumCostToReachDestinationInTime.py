# 1st solution
# O((n + m) * maxTime) time | O(n * maxTimes)
# where n = len(passingFees) and m = len(edges)
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        f = [[float("inf")] * n for _ in range(maxTime + 1)]
        f[0][0] = passingFees[0]
        for t in range(1, maxTime + 1):
            for i, j, cost in edges:
                if cost <= t:
                    f[t][i] = min(f[t][i], f[t - cost][j] + passingFees[i])
                    f[t][j] = min(f[t][j], f[t - cost][i] + passingFees[j])

        ans = min(f[t][n - 1] for t in range(1, maxTime + 1))
        return -1 if ans == float("inf") else ans