# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        sums = [0 for _ in range(n + 1)]
        for i in range(n):
            sums[i+1] = sums[i]
            if grumpy[i] == 0:
                sums[i+1] += customers[i]

        ans = 0
        total = sums[-1]
        count = 0
        for i in range(n):
            count += customers[i]
            j = max(0, i - minutes + 1)
            if j > 0:
                count -= customers[j - 1]
            t = count + total - sums[i+1] + sums[j]
            ans = max(ans, t)
        
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] = 0
        
        maxVal = cur = sum(customers[:minutes])
        for i in range(minutes, n):
            cur += customers[i] - customers[i - minutes]
            maxVal = max(maxVal, cur)
        
        return ans + maxVal