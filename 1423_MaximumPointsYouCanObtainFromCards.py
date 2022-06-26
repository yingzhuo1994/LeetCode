# 1st solution, sliding window
# O(n) time | O(1) space
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        m = n - k

        curTotal = 0
        for i in range(m):
            curTotal += cardPoints[i]
        
        minSum = curTotal
        for i in range(m, n):
            curTotal += cardPoints[i] - cardPoints[i-m]
            minSum = min(minSum, curTotal)
        return sum(cardPoints) - minSum