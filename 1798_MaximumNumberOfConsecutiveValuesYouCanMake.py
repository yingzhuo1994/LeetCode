class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        amount = 0
        for coin in coins:
            if coin > amount + 1:
                break
            amount += coin
        return amount + 1
