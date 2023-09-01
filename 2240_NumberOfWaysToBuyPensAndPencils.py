# 1st solution
# O(n // max(cost1, cost2)) time | O(1) space
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        a = total // cost1
        ans = 0
        for x in range(a + 1):
            money = total - cost1 * x
            y = money // cost2
            ans += y + 1
        return ans