# 1st solution
# O(n) time | O(n) space
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        close = -1
        penalty = float("inf")
        n = len(customers)
        counts = [0 for _ in range(n + 1)]
        count = 0
        for i, customer in enumerate(customers):
            if customer == "Y":
                count += 1
            counts[i + 1] = count
        
        for i, count in enumerate(counts):
            cost = i - count + counts[-1] - count
            if cost < penalty:
                close = i
                penalty = cost
        
        return close

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        close = -1
        penalty = float("inf")
        n = len(customers)

        total = 0
        for customer in customers:
            if customer == "Y":
                total += 1
        
        count = 0
        for i in range(n + 1):
            cost = i - count + total - count
            if cost < penalty:
                close = i
                penalty = cost
            if i < n and customers[i] == "Y":
                count += 1
        
        return close

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        h = m = s = 0
        for i, ch in enumerate(customers):  # [1] compute running profit where
            s += (ch == "Y") * 2 - 1        #     we add +1 for Y, -1 for N
            if s > m:                       # [2] keep track of the maximal 
                m, h = s, i+1               #     profit and its hour
        
        return h                            # [3] this is the hour with minimal penalty