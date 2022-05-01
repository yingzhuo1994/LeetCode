# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        sellBacklog, buyBacklog = [], []
        for price, amount, orderTupe in orders:
            if orderTupe == 0:
                heapq.heappush(buyBacklog, [-price, amount])
            else:
                heapq.heappush(sellBacklog, [price, amount])
            while sellBacklog and buyBacklog and sellBacklog[0][0] <= -buyBacklog[0][0]:
                dealAmount = min(buyBacklog[0][1], sellBacklog[0][1])
                buyBacklog[0][1] -= dealAmount
                sellBacklog[0][1] -= dealAmount
                if buyBacklog[0][1] == 0: heapq.heappop(buyBacklog)
                if sellBacklog[0][1] == 0: heapq.heappop(sellBacklog)
        orderNumber = 0
        for price, amount in sellBacklog:
            orderNumber += amount
            orderNumber %= MOD
        for price, amount in buyBacklog:
            orderNumber += amount
            orderNumber %= MOD
        return orderNumber