# 1st solution
# O(n) time | O(1) space
class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        mod = 10**9 + 7
        for k in range(2, n + 1):
            ans = (k* (2 * k - 1) * ans) % mod
        return ans