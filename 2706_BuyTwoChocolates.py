# 1st solution
# O(n) time | O(1) space
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = 101
        second = 102
        for price in prices:
            if price < first:
                first, second = price, first
            elif price < second:
                second = price
        left = money - first - second
        if left >= 0:
            return left
        else:
            return money