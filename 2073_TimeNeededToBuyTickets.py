# 1st solution
# O(n) time | O(1) space
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        ans = t
        for i in range(k):
            ans += min(tickets[i], t)
        for i in range(k+1, len(tickets)):
            ans += min(tickets[i], t - 1)
        return ans