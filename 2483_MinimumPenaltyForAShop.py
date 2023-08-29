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