# 1st solution
# O(n) time | O(1) space
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        ans = 0
        for i in range(len(tickets)):
            ans += min(tickets[i], t - (i > k))
        return ans