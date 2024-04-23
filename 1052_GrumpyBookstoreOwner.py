# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        sums = [0 for _ in range(n + 1)]
        counts = [0 for _ in range(n + 1)]
        for i in range(n):
            counts[i+1] = counts[i]
            if grumpy[i] == 0:
                counts[i+1] += customers[i]
            sums[i+1] = sums[i] + customers[i]

        ans = 0
        total = counts[-1]
        for i in range(n):
            j = max(0, i - minutes + 1)
            t = sums[i + 1] - sums[j] + total - counts[i+1] + counts[j]
            ans = max(ans, t)
        return ans
            