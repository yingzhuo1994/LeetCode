# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        stack = [[0, 0, 0]] + sorted(map(sorted, cuboids))
        dp = [0] * len(stack)
        for j in range(1, len(stack)):
            for i in range(j):
                if all(stack[i][k] <= stack[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + stack[j][2])
        return max(dp)