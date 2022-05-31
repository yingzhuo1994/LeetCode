# O(nlog(n)) time | O(log(n)) space
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        amount = 0
        for coin in coins:
            if coin > amount + 1:
                break
            amount += coin
        return amount + 1
