# 1st solution
# O(mn) time | O(mn) space
# where m = len(locations), n = fuel
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(idx, gas):
            if gas <= 0:
                return 0
            count = 0
            for i in range(len(locations)):
                if i == idx:
                    continue
                cost = abs(locations[i] - locations[idx])
                if gas >= cost:
                    count += dfs(i, gas - cost)
                    if i == finish:
                        count += 1
                    count %= MOD

            return count
        
        count = dfs(start, fuel)
        if start == finish:
            count += 1
        return count % MOD