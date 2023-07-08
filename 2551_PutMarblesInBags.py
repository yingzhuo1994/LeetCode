# 1st solution, MLE
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        @cache
        def dfs(start, end, d):
            if start > end:
                return float("inf"), float("-inf")
            if d == 0:
                cost = weights[start] + weights[end]
                return cost, cost
            minCost, maxCost = float("inf"), float("-inf")
            for left_k in range(d):
                right_k = d - 1 - left_k
                for idx in range(start + left_k, end - right_k):
                    leftMinCost, leftMaxCost = dfs(start, idx, left_k)
                    rightMinCost, rightMaxCost=  dfs(idx + 1, end, right_k)
                    minCost = min(minCost, leftMinCost + rightMinCost)
                    maxCost = max(maxCost, leftMaxCost + rightMaxCost)
            return minCost, maxCost
        
        minCost, maxCost = dfs(0, n - 1, k - 1)
        return maxCost - minCost