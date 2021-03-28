class Solution:
    # 1st brute-froce solution
    # def maxProfit(self, prices: List[int]) -> int:
    #     d = len(prices)
    #     lst = [0]
    #     for i in range(d):
    #         for j in range(i + 1, d):
    #             profit = prices[j] - prices[i]
    #             if profit > 0:
    #                 lst.append(profit)
    #     return max(lst)

    # 2nd sotution
    # def maxProfit(self, prices: List[int]) -> int:
    #     low = prices[0]
    #     maxProfit = 0
    #     for i, price in enumerate(prices):
    #         if price < low:
    #             low = price
    #         elif price - low > maxProfit:
    #             maxProfit = price - low
    #     return maxProfit

    # 3rd solution
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxProfit = 0
        for price in prices:
            if price < low:
                low = price
            profit = price - low
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
