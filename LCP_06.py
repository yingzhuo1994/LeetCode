class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0
        for coin in coins:
            q, r = divmod(coin, 2)
            ans += q + r
        return ans