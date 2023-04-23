# 1st solution, TLE
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(t):
            if len(t) == 1:
                num = int(t)
                if 0 < num <= k:
                    return 1
                return 0
            if t[0] == "0":
                return 0
            num = int(t)
            if num <= k:
                count = 1
            else:
                count = 0
            
            for i in range(1, len(t)):
                left = t[:i]
                right = t[i:]
                if left[0] == "0" or int(left) > k:
                    continue
                count += dfs(right)
                count %= MOD
            return count
        return dfs(s)