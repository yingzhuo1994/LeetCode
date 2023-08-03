# 1st solution, TLE
# O(10^n) time | O(10^n) space
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        @cache
        def dfs(keys):
            if all(key == 0 for key in keys):
                return 0
            ans = float("inf")
            for lst in special:
                p = lst[-1]
                if all(keys[i] >= lst[i] for i in range(n)):
                    ans = min(ans, p + dfs(tuple([keys[i] - lst[i] for i in range(n)])))
            for i in range(n):
                if keys[i] > 0:
                    lst = list(keys)
                    lst[i] -= 1
                    ans = min(ans, price[i] + dfs(tuple(lst)))
            return ans
        
        ans = dfs(tuple(needs))

        return ans 