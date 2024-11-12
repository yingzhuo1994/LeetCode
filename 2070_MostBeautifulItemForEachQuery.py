# 1st solution
# O(n * log(n) + q * log(n)) time | O(n + q) space
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        prices = []
        beauties = []
        items.sort()
        lastPrice = None
        for p, b in items:
            if p == lastPrice:
                beauties[-1] = max(beauties[-1], b)
            else:
                prices.append(p)
                beauties.append(b)
                if lastPrice is not None:
                    beauties[-1] = max(beauties[-1], beauties[-2])
            lastPrice = p
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prices, q) - 1
            if idx == -1:
                ans.append(0)
            else:
                ans.append(beauties[idx])
        return ans