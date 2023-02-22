# 1st solution
# O(k * (log(n))^2) time | O(n) space
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        if days >= n:
            return max(weights)
        
        minWeight = max(weights)
        maxWeight = sum(weights)
        for i in range(n - 1):
            weights[i + 1] += weights[i]
        weights = [0] + weights
        def canDivide(capacity):
            start = 0
            count = 0
            while start < n and count <= days:
                count += 1
                start = bisect.bisect_right(weights, weights[start] + capacity) - 1
            return count <= days


        while minWeight < maxWeight:
            midWeight = minWeight + (maxWeight - minWeight) // 2
            if canDivide(midWeight):
                maxWeight = midWeight
            else:
                minWeight = midWeight + 1
        return minWeight