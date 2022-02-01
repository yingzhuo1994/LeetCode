# 1st brute-froce solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = len(prices)
        lst = [0]
        for i in range(d):
            for j in range(i + 1, d):
                profit = prices[j] - prices[i]
                if profit > 0:
                    lst.append(profit)
        return max(lst)

# 2nd sotution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxProfit = 0
        for i, price in enumerate(prices):
            if price < low:
                low = price
            elif price - low > maxProfit:
                maxProfit = price - low
        return maxProfit

# 3rd solution
class Solution:
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

# 4th solution Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        for i in range(len(prices) - 1):
            profit.append(prices[i + 1] - prices[i])
            if profit[i] > 0:
                profit[i + 1] = profit[i] + profit[i + 1]
        return max(profit)

# 5th solution Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curProfit = 0
        maxProfit = 0
        for i in range(len(prices) - 1):
            singleProfit = prices[i + 1] - prices[i]
            if curProfit > 0:
                 curProfit += singleProfit
            else:
                curProfit = singleProfit
            if curProfit > maxProfit:
                maxProfit = curProfit
        return maxProfit

# 6th final simplified solution
# O(n) time | O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxProfit = 0
        for price in prices:
            if price < low:
                low = price
            if price - low > maxProfit:
                maxProfit = price - low
        return maxProfit
