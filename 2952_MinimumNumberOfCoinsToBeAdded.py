# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        curSum = 1
        count = 0
        i = 0
        while curSum < target + 1:
            if i < len(coins) and coins[i] <= curSum:
                curSum += coins[i]
                i += 1
            else:
                count += 1
                curSum += curSum

        return count