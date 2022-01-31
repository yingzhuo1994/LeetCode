# 1st solution
# O(m * n) time | O(1) space
# where m is the customer number and n is the bank number
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for account in accounts:
            ans = max(ans, sum(account))
        return ans