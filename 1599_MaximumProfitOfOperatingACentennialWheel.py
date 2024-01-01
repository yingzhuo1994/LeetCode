# 1st solution
# O(n) time | O(1) space
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost < runningCost:
            return -1

        maxProfit = -1
        ans = -1
        curBalance = 0
        waitingCustomers = 0
        i = 0
        while i < len(customers) or waitingCustomers > 0:
            if i < len(customers):
                customer = customers[i]
            else:
                customer = 0
            waitingCustomers += customer
            if waitingCustomers >= 4:
                curBalance += 4 * boardingCost
                waitingCustomers -= 4
            else:
                curBalance += waitingCustomers * boardingCost
                waitingCustomers = 0

            curBalance -= runningCost
            # print(i, curBalance, waitingCustomers)
            if curBalance > maxProfit:
                maxProfit = curBalance
                ans = i
            i += 1
        
        if maxProfit <= 0:
            return -1
        
        return ans + 1
            
