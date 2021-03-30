class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = prices[0]
        end = start
        for i, price in enumerate(prices):
            if price >= end and i < len(prices) - 1:
                end = price
            else:
                if price >= end:
                    profit += price - start
                elif end > start:
                    profit += end - start
                start = price
                end = start
        return profit
