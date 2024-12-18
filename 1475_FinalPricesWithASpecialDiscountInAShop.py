# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [prices[i] for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break
        return ans
            