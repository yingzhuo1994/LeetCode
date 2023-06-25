# 1st solution
# O(mn) time | O(mn) space
# where m = len(locations), n = fuel
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(idx, gas):
            if gas < 0:
                return 0
            count = 0
            if idx == finish:
                count += 1
            for i in range(len(locations)):
                if i == idx:
                    continue
                cost = abs(locations[i] - locations[idx])
                count += dfs(i, gas - cost)
                count %= MOD

            return count
        
        return dfs(start, fuel)