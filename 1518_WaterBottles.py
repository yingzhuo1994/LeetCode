# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            q, r = divmod(numBottles, numExchange)
            ans += q
            numBottles = q + r
        return ans